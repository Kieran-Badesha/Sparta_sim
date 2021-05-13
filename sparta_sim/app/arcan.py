from numpy.random import binomial
from pprint import pprint
from classes import trainee_generator


def placing_trainees(months):
    # months = 12
    index = 0
    business = []
    java = []
    csharp = []
    data = []
    dev = []

    b_grads = 0
    c_grads = 0
    da_grads = 0
    de_grads = 0
    j_grads = 0

    while index != months + 1:
        group = trainee_generator(20, 30)
        for i in group['Business']['Count']:
            business.append(i)
            # pprint(business)
            if len(business) == 13:
                b_grads += business[0]
                business.pop(0)
                pprint(f"{b_grads} = b_grads")
                # pprint(business)
            # pprint(business)
        for i in group['CSharp']['Count']:
            csharp.append(i)
            if len(csharp) == 13:
                c_grads += csharp[0]
                csharp.pop(0)
                pprint(f"{c_grads} = c_grads")
                # pprint(csharp)
            # pprint(csharp)
        for i in group['Data']['Count']:
            data.append(i)
            if len(data) == 13:
                da_grads += data[0]
                data.pop(0)
                pprint(f"{da_grads} = da_grads")
            # pprint(data)
        for i in group['DevOps']['Count']:
            dev.append(i)
            if len(dev) == 13:
                de_grads += dev[0]
                dev.pop(0)
                pprint(f"{de_grads} = de_grads")
            # pprint(dev)
        for i in group['Java']['Count']:
            java.append(i)
            if len(java) == 13:
                j_grads += java[0]
                java.pop(0)
                pprint(f"{j_grads} = j_grads")
            # pprint(java)
        if index == months:
            cohort = {'Business': business,
                      'Csharp': csharp,
                      'Data': data,
                      'DevOps': dev,
                      'Java': java
                    }

            return cohort
            # pprint(cohort)
        # pprint(group)
        # pprint(group['Business']['Count'])
        index += 1


pprint(placing_trainees(16))


# def warming_the_bench(months):
#     b_grads = 0
#     c_grads = 0
#     data_grads = 0
#     dev_grads = 0
#     j_grads = 0
#     graduated = placing_trainees(months)
#     pprint(graduated)
#     print(len(graduated['Business']))
#     if len(graduated['Business']) >= 13:
#         b_grads += graduated['Business'][0]
#         graduated['Business'].pop()
#         print(b_grads)
#         print(graduated['Business'])
#     # if len(graduated['Csharp']) == 13:
#     #     c_grads += graduated['Csharp'][0]
#     #     del graduated['Csharp'][0]
#     #
#     # if len(graduated['Data']) == 13:
#     #     data_grads += graduated['Data'][0]
#     #     del graduated['Data'][0]
#     #
#     # if len(graduated['DevOps']) == 13:
#     #     dev_grads += graduated['DevOps'][0]
#     #     del graduated['DevOps'][0]
#     # if len(graduated['Java']) == 13:
#     #     j_grads += graduated['Java'][0]
#     #     del graduated['Java'][0]
#     return graduated
#
#
# a = warming_the_bench(13)


