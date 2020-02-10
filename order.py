from color import *

print("hello", red("ljm"), "!")
print("hello", green("ljm"), "!")
print("hello", blue("ljm"), "!")

poet_key = "poet"
title_key = "title"
poem_key = "poem"

poem_cnt_show = 10

poems = []
f = open("poems.txt", "r", encoding="utf-8")
lines = f.readlines()
for line in lines:
    try:
        poems.append(eval(line))
    except:
        pass

while True:
    orders_str = input("输入飞花令（以空格区分）：")
    poem_cnt_show = 10
    orders = orders_str.split(" ")
    orders_cnt = len(orders)
    poem_cnt = 0
    for poem in poems:
        poem_sentences = poem[poem_key]
        if orders_cnt == 1:
            if orders[0] in poem_sentences:
                poem_cnt += 1
                poem_sentences = poem_sentences.replace(orders[0], red(orders[0]))
                poem_sentences = poem_sentences.replace("。", "。\n")
                print("{} {}\n{}\n".format(green(poem[title_key]), poem[poet_key], poem_sentences))
                if poem_cnt == poem_cnt_show:
                    go_on_flag = input("是否继续显示？(Y/n)")
                    if go_on_flag == "" or go_on_flag == "Y" or go_on_flag == "y":
                        poem_cnt_show += 1
                        continue
                    else:
                        break
                # poem_port = poem_sentences.split(orders[0])
                # poem_mark = ""
                # for i in range(len(poem_port)):
                #     poem_mark += poem_port
                #     if i != len(poem_port)-1:
                #         poem_mark += red(orders[0])
        if orders_cnt == 2:
            poem_sentences = poem_sentences.replace("。", "。\n")
            poem_ports = poem_sentences.split("\n")
            poem_find_flag = 0
            for poem_port in poem_ports:
                if orders[0] in poem_port and orders[1] in poem_port:
                    poem_find_flag = 1
                    break
            if poem_find_flag == 1:
                poem_cnt += 1
                poem_sentences = poem_sentences.replace(orders[0], red(orders[0]))
                poem_sentences = poem_sentences.replace(orders[1], blue(orders[1]))
                print("{} {}\n{}\n".format(green(poem[title_key]), poem[poet_key], poem_sentences))
                if poem_cnt == poem_cnt_show:
                    go_on_flag = input("是否继续显示？(Y/n)")
                    if go_on_flag == "" or go_on_flag == "Y" or go_on_flag == "y":
                        poem_cnt_show += 1
                        continue
                    else:
                        break    

            # if orders[0] in poem_sentences and orders[1] in poem_sentences:
            #     poem_sentences = poem_sentences.replace("。", "。\n")

            #     poem_cnt += 1
            #     poem_sentences = poem_sentences.replace(orders[0], red(orders[0]))
            #     poem_sentences = poem_sentences.replace(orders[1], blue(orders[1]))
            #     print("{} {}\n{}\n".format(green(poem[title_key]), poem[poet_key], poem_sentences))
            #     if poem_cnt == poem_cnt_show:
            #         go_on_flag = input("是否继续显示？(Y/n)")
            #         if go_on_flag == "" or go_on_flag == "Y" or go_on_flag == "y":
            #             poem_cnt_show += 1
            #             continue
            #         else:
            #             break



