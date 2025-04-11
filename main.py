from db import init_db
from farmer_advisor import analyze_farmer_input
from market_researcher import find_best_crop
from ai_model import ai_analysis

def run_system():
    print(" Multi-Agent AI System for Sustainable Agriculture")
    init_db()

    farmer_data = analyze_farmer_input()
    if farmer_data:
        find_best_crop(farmer_data)
        ai_advice = ai_analysis(farmer_data)
        print(" AI Advice for Farmers:", ai_advice)
    else:
        print(" Please add farmer input to proceed.")

if __name__ == "__main__":
    run_system()
