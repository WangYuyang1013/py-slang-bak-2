# # def is_divisible(x, y):
# #     return x % y == 0

# # def has_factor(n, i):
# #     return False if i * i > n else is_divisible(n, i) or has_factor(n, i + 1)

# # def is_prime(n):
# #     return False if n < 2 else not has_factor(n, 2)

# # is_prime(8)

# def evaluate_loan_application(
#     income,
#     credit_score,
#     loan_amount,
#     property_value,
#     co_signer_available,
#     has_criminal_record,
#     existing_debt,
#     savings,
#     short_term_liabilities,
#     repeated_late_payments
# ):
#     # 如果收入小于 0，认为申请信息无效
#     if income < 0:
#         return "invalid"
#     else:
#         # 信用分小于 300，直接拒绝
#         if credit_score < 300:
#             return "reject"
#         else:
#             # 如果有犯罪记录，且有逾期还款历史，多半拒绝
#             if has_criminal_record:
#                 if repeated_late_payments:
#                     return "reject"
#                 else:
#                     return "review"
#             else:
#                 # 信用分大于 700 且储蓄大于现有债务 -> 优先批准
#                 if credit_score > 700:
#                     if savings > existing_debt:
#                         return "approve"
#                     else:
#                         # 若储蓄不够覆盖债务，但有担保人 -> 进入人工复审
#                         if co_signer_available:
#                             return "review"
#                         else:
#                             return "reject"
#                 else:
#                     # 信用分不高于700，则看收入与房产价值
#                     if loan_amount < income:
#                         # 房产价值大于贷款额的2倍 -> 有较好抵押
#                         if property_value > loan_amount * 2:
#                             return "approve"
#                         else:
#                             return "review"
#                     else:
#                         return "reject"

# # ---------- 测试函数示例 ----------

# def test_loan_case_1():
#     # 场景1：收入、信用分、抵押物都不错，且有一定储蓄
#     result = evaluate_loan_application(
#         5000,   # income
#         710,    # credit_score
#         2000,   # loan_amount
#         5000,   # property_value
#         False,  # co_signer_available
#         False,  # has_criminal_record
#         1000,   # existing_debt
#         3000,   # savings
#         500,    # short_term_liabilities
#         False   # repeated_late_payments
#     )
#     if result == "approve":
#         return "test_loan_case_1 pass"
#     else:
#         return "test_loan_case_1 fail"

# def test_loan_case_2():
#     # 场景2：信用分极低，直接拒绝
#     result = evaluate_loan_application(
#         4000,
#         250,
#         1000,
#         3000,
#         False,
#         False,
#         500,
#         2000,
#         300,
#         False
#     )
#     if result == "reject":
#         return "test_loan_case_2 pass"
#     else:
#         return "test_loan_case_2 fail"

# def test_loan_case_3():
#     # 场景3：无犯罪记录，但收入不足贷款，且信用分不高，需要看房产
#     result = evaluate_loan_application(
#         3000,
#         650,
#         3500,
#         6000,
#         False,
#         False,
#         0,
#         500,
#         500,
#         False
#     )
#     if result == "review":
#         return "test_loan_case_3 pass"
#     else:
#         return "test_loan_case_3 fail"

# def test_loan_case_4():
#     # 场景4：有犯罪记录但是没有逾期还款记录 -> review
#     result = evaluate_loan_application(
#         4500,
#         680,
#         2000,
#         4000,
#         False,
#         True,   # has_criminal_record
#         100,
#         1000,
#         200,
#         False   # repeated_late_payments
#     )
#     if result == "review":
#         return "test_loan_case_4 pass"
#     else:
#         return "test_loan_case_4 fail"

# def run_some_tests():
#     r1 = test_loan_case_1()
#     r2 = test_loan_case_2()
#     r3 = test_loan_case_3()
#     r4 = test_loan_case_4()

#     summary = r1 + "\n" + r2 + "\n" + r3 + "\n" + r4
#     return summary

# print(run_some_tests())
# run_some_tests()

math_isnan("9")