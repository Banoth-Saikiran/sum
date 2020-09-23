#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')

def xyz():
    return render_template('sum.html')
@app.route('/sum', methods=['GET','POST'])

def abc():
    if(request.method=='POST'):
        num1=int(request.form['n1'])
        num2=int(request.form['n2'])
        total=num1+num2
        print(total)
        return render_template('sum.html',total=result)
if __name__=='__main__':
    app.run()





