import jieba
import wordcloud

f=open("工作报告.txt","r",encoding="utf-8")

t=f.read()
f.close()
ls=jieba.lcut(t)

txt=" ".join(ls)
w=wordcloud.WordCloud( font_path="msyh.ttc",\
                       width=1000,height=700,\
                       background_color="white",\
                        max_words=200,\
                       stopwords={"我","的","他","在"\
                                  "了","鲍伯","兰德",\
                                  "是","就","我们","因为"\
                                  "也","将","地","只能","甚至"\
                                  "嗯","没有","上"}
                       )

w.generate(txt)
w.to_file("pywcloud3.png")