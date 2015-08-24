"""“I was driving on the highway the other day and I happened to notice my odometer.
Like most odometers, it shows six digits, in whole miles only. So, if my car had
300,000 miles, for example, I’d see 3-0-0-0-0-0.
“Now, what I saw that day was very interesting. I noticed that the last 4 digits
were palindromic; that is, they read the same forward as backward. For example,
5-4-4-5 is a palindrome, so my odometer could have read 3-1-5-4-4-5.
“One mile later, the last 5 numbers were palindromic. For example, it could have
read 3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were
palindromic. And you ready for this? One mile later, all 6 were palindromic!

“The question is, what was on the odometer when I first looked?”"""

def is_palindrome(num):
    return str(num) == str(num)[::-1]


def car_talk_8():
    for num in range(100000, 1000000):
        if is_palindrome(str(num)[2:6]):
            if is_palindrome(str(num + 1)[1:6]):
                if is_palindrome(str(num + 2)[1:5]):
                    if is_palindrome(str(num +3)):
                        print num
    return False

car_talk_8()