#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator

# In[23]:


name = input('Enter your name: ')

weight = int(input('Enter your weight in pounds: '))

height = int(input('Enter your height in inches: '))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI >= 0:
    if(BMI < 18.5):
        print(name + ', you are underweight. Perhaps you should eat more.')
    elif (BMI <= 24.9):
        print(name + ', you are normal weight. Keep it up.')
    elif (BMI <= 29.9):
        print(name + ', you are overweight. Perhaps you should eat a salad.')
    elif(BMI <= 34.9):
        print(name + ', you are obese. You should start a diet.')
    elif(BMI <= 39.9):
        print(name + ', you are severely obese. You should definitely see a nutritionist.')
    else:
        print(name + ', you are morbidly obese. The end is nigh')


# In[ ]:


#Logic and formula:


# In[ ]:


#BMI = (weight * 703) / (height * height)


# In[ ]:


Under 18.5  	  Underweight   	  Minimal
18.5 - 24.9 	  Normal Weight 	  Minimal
25 - 29.9   	  Overweight    	  Increased
30 - 34.9   	  Obese 	  High
35 - 39.9   	  Severely Obese    	  Very High
40 and over 	  Morbidly Obese    	  Extremely High

