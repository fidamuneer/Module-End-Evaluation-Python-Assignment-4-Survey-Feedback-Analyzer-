feedback_data = {
    "S_No" : [1,2,3,4,5,6,7,8,9,10] ,
    "Name" : ["Ravi" , "Meera" , "Sam" , "Anu" , "Raj" , "Divya" , "Arjun" , "Kiran" , "Leela" , "Nisha"] ,
    "Feedback" : [
        "Very GOOD Service!!!",
        "poor support, not happy ",
        "GREAT experience! will come again." ,
        "okay okay...",
        "not BAD",
        "Excellent care, excellent staff!" ,
        "good food and good ambience!" ,
        "Poor response and poor handling of issue" ,
        "Satisfied. But could be better." ,
        "Good support... quick service."
        ],
    "Rating" : [5,2,5,3,2,5,4,1,3,4]
    }
print(feedback_data)

n = int(input("How many feedbacks do you want to add?"))
for i in range(n):
    name = input("Enter customer name: ")
    feedback = input("Enter your feedback: ")
    rating = int(input("Enter rating (1-5): "))
    
    S_no = len(feedback_data["S_No"])+1
    feedback_data["S_No"].append(S_no)
    feedback_data["Name"].append(name)
    feedback_data["Feedback"].append(feedback)
    feedback_data["Rating"].append(rating)
print(feedback_data)

#cleaning
for i in range(len(feedback_data["Feedback"])):
    x = feedback_data["Feedback"][i]
    x = x.replace(".","")
    x = x.replace(",","")
    x = x.replace("?","")
    x = x.replace("!","")
    x = " ".join(x.split())
    x = x.lower()
    feedback_data["Feedback"][i] = x
print(feedback_data)

#Word Count Insights
def count_word_in_feedbacks(word):
    count = 0
    for i in feedback_data["Feedback"]:
        words = i.split()
        if word.lower() in words:
            count = count+1
    return count
 
print(count_word_in_feedbacks("good"))
print(count_word_in_feedbacks("poor"))
print(count_word_in_feedbacks("excellent"))

#Final Summary
print(feedback_data)

#Average Rating
total = sum(feedback_data["Rating"])
count = len(feedback_data["Rating"])
average_rating = total/count
print("Avg_rating:",average_rating)

#Finding Longest Feedback 
longest_feedback = ""
max_count = 0

for i in feedback_data["Feedback"]:
    count = len(i.split())
    if count > max_count:
        max_count = count
        longest_feedback = i

print(longest_feedback)


# Unique words
unique_words = set()
for i in feedback_data["Feedback"]:
    words = i.split()
    unique_words.update(words)
print(unique_words)

# Sorted feedbacks by rating

a = zip(feedback_data["Rating"], feedback_data["Name"], feedback_data["Feedback"])

sorted_data = sorted(a, reverse=True)

for i in sorted_data:
    print(i)
