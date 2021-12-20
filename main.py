# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dict_v = {0: 3, 1: 6, 2: 8, 3: 9}
    dict_e = dict(dict())
    dict_e[0] = {1: 236, 2: 564, 3: 56}
    dict_e[1] = {0: 4, 3: 7, 2: 564}
    dict_e[2] = {3: 8, 0: 564, 1: 564}
    ans = dict()
    if 6 not in dict_v:
        print("h1")
    for i in dict_e.keys():
        if 2 in dict_e[i]:
            ans[i]=dict_v[i]



    print(ans)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
