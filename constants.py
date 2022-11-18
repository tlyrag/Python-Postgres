insertDrink = """
    INSERT INTO public.starbucksgame(
        "Drink_Type", "Drink_Type_Link", "Coffee_Name", "Coffee_Name_Url", "Ingredients")
        VALUES (%s, %s, %s, %s, %s);
"""
selectDrink = """
    Select * 
    from public.starbucksgame
    where
    "Drink_Type" = (%s)
    
"""