# 1: Preloaded Feedbacks (Given data)

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Teela', 'Nisha'],
    'Feedback': [
        'Very GOOD Service!!!',
        'poor support,    not happy   ',
        'GREAT experience! will come again.',
        'okay    okay...',
        '    not    BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

# 2: Add more Feedbacks

n = int(input("How many more feedbacks do you want to add? "))

s_no = 11

for i in range(n):
    print("S_No:", s_no)
    name = input("Enter your name: ")          
    feedback = input("Enter your feedback: ") 
    rating = int(input("Enter your rating (1-5): "))

    feedback_data['S_No'].append(s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

    s_no = s_no + 1  


# 3: Text Cleaning

for i in range(len(feedback_data['Feedback'])):

    feedback = feedback_data['Feedback'][i]

    # Remove punctuation
    feedback = feedback.replace(".", "")
    feedback = feedback.replace(",", "")
    feedback = feedback.replace("!", "")
    feedback = feedback.replace("?", "")

    # Replace multiple spaces with one space
    feedback = " ".join(feedback.split())

    # Remove leading and trailing spaces
    feedback = feedback.strip()

    # Convert to lowercase
    feedback = feedback.lower()

    # Store the cleaned feedback
    feedback_data['Feedback'][i] = feedback

    # print(feedback_data['Feedback'])    # To check is the cleaning process working use this 

# 4: Word Count Insights

def count_word_in_feedbacks(word):
    count = 0

    for feedback in feedback_data['Feedback']:
        if word.lower() in feedback.lower():
            count = count + 1

    return count


print("Number of feedbacks containing 'good':", count_word_in_feedbacks("good"))
print("Number of feedbacks containing 'poor':", count_word_in_feedbacks("poor"))
print("Number of feedbacks containing 'excellent':", count_word_in_feedbacks("excellent"))  


# 5: Final Summary & Insights

# Display final cleaned feedback_data
print("\nFinal Cleaned Feedback Data:")
print(feedback_data)


# Average rating
average_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print("\nAverage Rating:", average_rating)


# Find feedback with longest comment
longest_feedback = ""
longest_word_count = 0

for feedback in feedback_data['Feedback']:
    word_count = len(feedback.split())

    if word_count > longest_word_count:
        longest_word_count = word_count
        longest_feedback = feedback

print("\nFeedback with the longest comment:")
print(longest_feedback)
print("Word count:", longest_word_count)


# Unique words across all feedbacks
unique_words = set()

for feedback in feedback_data['Feedback']:
    words = feedback.split()
    unique_words.update(words)

print("\nUnique words used across all feedbacks:")
print(unique_words)

# Optional: Sort feedbacks by rating

sorted_feedbacks = sorted(
    zip(feedback_data['Name'], feedback_data['Feedback'], feedback_data['Rating']),
    key=lambda x: x[2],
    reverse=True
)

print("\nFeedbacks sorted by rating:")
print(sorted_feedbacks)