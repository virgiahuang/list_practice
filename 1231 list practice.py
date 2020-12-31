#list 清單
#在python裡面用 [ ] 表示清單，用[ ] 當成清單的容器，把內容裝進去

# a = [ ] # <-- 空清單
a = ['Chanel', 'Dior' ,'Louis Vuitton'] #<-- 用逗號隔開項目，清單內容可以是任何值（佈林值，數字，字串，或者是浮點數）
#清單的index (索引)是從0開始，以上面的清單為例，Chanel 是 0, Dior 是 1, Louis Vuitton 是 2
print (a) #會印出所有項目
print (a[1]) # 只會印出Dior
a.append ('Hermes') #a.append 是加入新項目到清單裡面，“.“ 是”的“的意思，append 是一個函式（功能）-->a.append ('Hermes') 意思就是把Hermes 裝進a清單裡面
print (a)
print (a[3])
len (a) #len 是 length 的縮寫-->程式碼意思是 a 清單的長度
print (len(a))
#檢查項目在不在清單裡面 用 in
'Chanel' in a 
print ('Chanel' in a ) #檢查Chanel 在不在清單裡面  -->是非題 True or False
print ('DKNY' in a )