# coding: utf-8

from langid.langid import LanguageIdentifier, model

# 已处理的行计数
i = 0

# 打开文件
with open('tweetstream.2013. Jan22-29.csv', 'r') as fileread, open('tweet_english.txt', 'w') as filewrite:
    try:
        identifier = LanguageIdentifier.from_modelstring(
            model, norm_probs=True)
        # 遍历行，这里使用迭代器
        for line in fileread:
            linelist = line.split(',')
            # 取得 Tweet 的内容，去掉头尾的"|"
            tweet_content = linelist[4][1:-1]
            # 验证内容的语言
            classify_result = identifier.classify(tweet_content)
            # 是英文则写入新的文件
            if classify_result[0] == 'en' and classify_result[1] > 0.99:
                tweet_content = tweet_content + '\n'
                filewrite.writelines(tweet_content)

            i = i + 1
            if i % 100000 == 0:
                print '已处理了 {0} 行'.format(i)
    except Exception as ex:
        print ex.args[0]
