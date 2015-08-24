"""Write a function called eval_loop that iteratively prompts the user,
takes the resulting input and evaluates it using eval, and prints the result.
It should continue until the user enters ‘done’, and then return the value
of the last expression it evaluated."""

def eval_loop():
    current_result = ''
    while True:
        to_evaluate = raw_input(">>")
        if to_evaluate == "done":
            break
        current_result = eval(to_evaluate)
        print current_result
    return current_result