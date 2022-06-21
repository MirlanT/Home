from django.shortcuts import render
from collections import Counter


def index_view(request):
    query = request.POST.getlist("name")
    return render(request, 'index.html')

lis = []
class Check():
    def __init__(self, numbers) -> None:
        self.secret_nums = [5, 1, 2, 9]
        self.numbers = numbers

    def check_for_print(self):
        for i in self.numbers:
            if i > 9 or i < 0:
                return "Number must be 1-9"
        a = set(self.numbers)
        try:
            if len(a) > 4:
                return "Enter less than 4"
            elif len(a) < 4:
                return "Enter more than 4 or Not-enter dublicate number"
        except ValueError:
            return "enter number please"
        # elif len(a) == 2 or len(a) == 3:
        #     return "enter note number"

    def guess_numbers(self):
        bulls = 0
        cows = 0
        if self.numbers == self.secret_nums:
            return "Correct"
        else:
            for i in range(len(self.secret_nums)):
                if self.secret_nums[i] == self.numbers[i]:
                    bulls += 1
                elif self.numbers[i] in self.secret_nums:
                    cows += 1
            return f"You got  {bulls} bulls, {cows} cows"


def create_article(request):
    if request.method == "GET":
        return render(request, 'create.html')
    else:
        numbers = list(map(int, request.POST.get('numbers').split()))
        check = Check(numbers)

        if check.check_for_print():
            first_function = check.check_for_print()
            contex = {
                "red": first_function
            }
            return render(request, 'create.html', contex)
        else:
            second_function = check.guess_numbers()
            lis.append(check.guess_numbers)
            contex = {
                "red": second_function,
            }
            return render(request, 'create.html', contex)


def index_view10(request):
    contex = {
        'lst': lis
    }
    return render(request, 'index10.html', contex)



