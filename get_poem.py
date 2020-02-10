from selenium import webdriver
import time


chrome_driver="D:\\Program Files\\Chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get('http://www.shicimingju.com/category/all')


f = open("poems.txt", "a+", encoding="utf-8")


poet_page = 0
height = 30
while True:
    poet_page += 1
    if poet_page > 5:
        break
    Poets = []
    poets = driver.find_elements_by_class_name("zuozhe_list_item")
    for poet in poets:
        Poets.append(poet.text.split("\n")[0])
        print(poet.text.split("\n")[0])
    for poet in Poets:
        if poet == "[宋]李清照" or poet == "[先秦]诗经" or poet == "[宋]苏轼" or poet == "[唐]李白":
            continue
        while True:
            try:
                driver.find_element_by_link_text(poet).click()
                break
            except:
                js = "window.scrollBy(0,{});".format(height)
                driver.execute_script(js)
        handles = driver.window_handles
        driver.switch_to_window(handles[1])
        poem_page = 0
        while True:
            poem_page += 1
            if poem_page > 3:
                break
            poems = driver.find_elements_by_class_name("shici_list_main")
            for poem in poems:
                poem_kv = "{"
                poem_kv += u'"poet":"{}",'.format(poet)
                name = poem.find_element_by_tag_name("h3").text
                poem_kv += u'"title":"{}",'.format(name)
                content = poem.find_element_by_class_name("shici_content")
                poem_sentence_cnt = 0
                while True:
                    try:
                        more = content.find_element_by_link_text("展开全文")
                        js = "window.scrollBy(0,{});".format(height)
                        driver.execute_script(js)
                    except:
                        break
                    try:
                        more.click()
                        break
                    except:
                        continue
                p = content.text
                poem_sentences = p.split("\n")
                poem_sentence_cnt = len(poem_sentences)
                if poem_sentences[poem_sentence_cnt-1] == "收起":
                    poem_sentence_cnt -= 1
                poem_content = ""
                for i in range(poem_sentence_cnt):
                    poem_content += poem_sentences[i]
                poem_kv += u'"poem":"{}"'.format(poem_content)
                poem_kv += "}\n"
                print(poem_kv)
                f.write(poem_kv)
            try:
                driver.find_element_by_link_text("下一页").click()
            except:
                break
        driver.close()
        handles = driver.window_handles
        driver.switch_to_window(handles[0])
    try:
        driver.find_element_by_link_text("下一页").click()
    except:
        break
f.close()

# driver.find_element_by_id("su").click()

