import tkinter as tk
from tkinter import messagebox

def calculate_npv():
    try:
        messagebox.showinfo("안내", "안녕하세요!")
        initial_investment = float(entry_initial.get())
        discount_rate = float(entry_discount.get()) / 100
        cash_flows = list(map(float, entry_cashflows.get().split(',')))
        
        npv = -initial_investment
        for i, cash_flow in enumerate(cash_flows):
            npv += cash_flow / ((1 + discount_rate) ** (i + 1))
        
        messagebox.showinfo("결과", f"순현재가치(NPV): {npv:.2f}")
    except ValueError:
        messagebox.showerror("입력 오류", "올바른 숫자를 입력하세요.")

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("NPV 계산기")
root.geometry("400x300")

# 초기 투자 비용 입력
tk.Label(root, text="초기 투자 비용:").pack()
entry_initial = tk.Entry(root)
entry_initial.pack()

# 할인율 입력
tk.Label(root, text="할인율 (%):").pack()
entry_discount = tk.Entry(root)
entry_discount.pack()

# 현금 흐름 입력
tk.Label(root, text="현금 흐름 (쉼표로 구분):").pack()
entry_cashflows = tk.Entry(root)
entry_cashflows.pack()

# 계산 버튼
btn_calculate = tk.Button(root, text="NPV 계산", command=calculate_npv)
btn_calculate.pack()

# 메인 루프 실행
root.mainloop()
