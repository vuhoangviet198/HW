def main():
    # Default: A is correct answer
    qa = [
        ('Q1', 'A'),('Q2', 'A'),('Q3', 'A'),('Q4', 'A'),('Q5', 'A'),
        ('Q6', 'A'),('Q7', 'A'),('Q8', 'A'),('Q9', 'A'),('Q10', 'A'),
        ('Q11', 'A'),('Q12', 'A'),('Q13', 'A'),('Q14', 'A'),('Q15', 'A'),
        ('Q16', 'A'),('Q17', 'A'),('Q18', 'A'),('Q19', 'A'),('Q20', 'A'),
    ]

#Initialize:
    #number of correct answers:
    num_correct = 0
    #list of incorrect answers:
    q_incorrect= []

# Get user input and update correct answer (-> num_correct = 0) + store incorrect answer (-> q_incorrect = [])
    temp = 1
    for q,a in qa:
        while True:  # Keep getting input from the user
            abcd = ["A", "B", "C", "D"]
            try:
                user_answer =  input(q + ": ")
                if user_answer not in abcd: #Input restriction (only A, B, C, D)
                    print('Answer is invalid, please re-input the answer!')
                    continue
                else:
                    if user_answer == a:
                        num_correct += 1 #Update total of correct answer to the variable (num_correct)
                    else:
                        q_incorrect.append(temp) #Store incorrect answer to the list (q_incorrect)
                    temp = temp + 1
                    break
            except ValueError:
                print('Conversion error, please re-input the answer!')
                continue

# print result
    # passed/failed
    print("Result: ", end="")
    if num_correct >= 15:
        print("Passed")
    else:
        print("False")
    #total correct answers
    print('Total correct:', num_correct)
    #incorrect questions
    print('Incorrect Questions: ', end="")
    print(*q_incorrect, sep=", ")
    #total incorrect answers
    print('Total incorrect:', len(q_incorrect))

main()