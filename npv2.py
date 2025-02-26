import tkinter as tk
from tkinter import messagebox

def calculate_npv():
    try:
        messagebox.showinfo("안내", "안녕하세요!")
        initial_investment = float(entry_initial.get())
        discount_rate = float(entry_discount.get()) / 100
        operating_income = float(entry_operating_income.get())
        depreciation = float(entry_depreciation.get())
        ebit = float(entry_ebit.get())
        net_income = float(entry_net_income.get())
        working_capital = float(entry_working_capital.get())
        capex = float(entry_capex.get())
        
        cash_flows = [operating_income, depreciation, ebit, net_income, working_capital, -capex]
        
        npv = -initial_investment
        for i, cash_flow in enumerate(cash_flows):
            npv += cash_flow / ((1 + discount_rate) ** (i + 1))
        
        messagebox.showinfo("결과", f"순현재가치(NPV): {npv:.2f}")
    except ValueError:
        messagebox.showerror("입력 오류", "올바른 숫자를 입력하세요.")

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("NPV 계산기")
root.geometry("400x500")

# 초기 투자 비용 입력
tk.Label(root, text="초기 투자 비용:").pack()
entry_initial = tk.Entry(root)
entry_initial.pack()

# 할인율 입력
tk.Label(root, text="할인율 (%):").pack()
entry_discount = tk.Entry(root)
entry_discount.pack()

# 영업이익 입력
tk.Label(root, text="영업이익:").pack()
entry_operating_income = tk.Entry(root)
entry_operating_income.pack()

# 감가상각비 입력
tk.Label(root, text="감가상각비:").pack()
entry_depreciation = tk.Entry(root)
entry_depreciation.pack()

# 세전이익 입력
tk.Label(root, text="세전이익 (EBIT):").pack()
entry_ebit = tk.Entry(root)
entry_ebit.pack()

# 세후 순이익 입력
tk.Label(root, text="세후 순이익:").pack()
entry_net_income = tk.Entry(root)
entry_net_income.pack()

# 운전자본 변화 입력
tk.Label(root, text="운전자본 변화:").pack()
entry_working_capital = tk.Entry(root)
entry_working_capital.pack()

# 자본지출 입력
tk.Label(root, text="자본지출 (CapEx):").pack()
entry_capex = tk.Entry(root)
entry_capex.pack()

# 계산 버튼
btn_calculate = tk.Button(root, text="NPV 계산", command=calculate_npv)
btn_calculate.pack()

# 메인 루프 실행
root.mainloop()

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def npv_calculator():
    result = None
    if request.method == 'POST':
        try:
            initial_investment = float(request.form['initial_investment'])
            discount_rate = float(request.form['discount_rate']) / 100
            investment_years = int(request.form['investment_years'])
            operating_income = float(request.form['operating_income'])
            depreciation = float(request.form['depreciation'])
            ebit = float(request.form['ebit'])
            net_income = float(request.form['net_income'])
            working_capital = float(request.form['working_capital'])
            capex = float(request.form['capex'])
            
            cash_flows = [operating_income, depreciation, ebit, net_income, working_capital, -capex]
            npv = -initial_investment
            for year in range(1, investment_years + 1):
                for cash_flow in cash_flows:
                    npv += cash_flow / ((1 + discount_rate) ** year)
            
            result = f"순현재가치(NPV): {npv:.2f}"
        except ValueError:
            result = "올바른 숫자를 입력하세요."
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
