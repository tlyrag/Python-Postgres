sql1 = """
    INSERT INTO public.starbucksgame(
        "Drink_Type", "Drink_Type_Link", "Coffee_Name", "Coffee_Name_Url", "Ingredients")
        VALUES (%s, %s, %s, %s, %s);
"""