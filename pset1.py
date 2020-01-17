#!/usr/bin/env python
# coding: utf-8

# In[4]:


anual_salary=float(input("Enter   your annual Salary:"))

portion_saved =float(input("Enter the portion of your salary to save , as a decimal:"))
total_cost= float(input ("Enter the cost of your dream home:"))
down_payment_percentage =total_cost* 0.12 
print("A",down_payment_percentage)
current_savings=0
r= 0.05/12
months=1
monthly=(1+portion_saved)(anual_salary/12)
print(monthly)
#current_savings=anual_salery* portion_saved
#ms= current_savings /12
#return_rate=current_savings*r
total=total_cost-down_payment_percentage
print("B",total)


#current_savings!=total 
while  current_savings<total :
    current_savings+= monthly+(current_savings*(r)) 

    months+=1
    #print("c",months,current_savings)

print("number of months",months)


# In[5]:


ans=float(input("anns"))
ps= float(input("portionS"))
tc=float(input("house"))
dowpp=0.12
cs=0
m=0
r=0.05

ps*=(ans/12)
dp=tc*dowpp
while cs<dp:
    cs+=(ps+(cs*(r/12)))
    m+=1
print("nom",m)


# In[5]:


ans=float(input("anns"))
ps= float(input("portionS"))
tc=float(input("house"))
sar=float(input("semi anual"))
dowpp=0.12
cs=0
m=0
r=0.05


dp=tc*dowpp

while cs<dp:
    cs+=((ans/12)*ps +cs*(r/12))
    m+=1
    if m%6==0:     
        ans += ans * sar
        
print("nom",m)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




