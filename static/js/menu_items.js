const menuData = {

    "Welcome Drinks": [
        "Fresh Juice Live Counter",
        "Welcome Drinks Assorted"
    ],

    "Soup Counter": [
        "Sweet Corn Chicken Soup",
        "Hot & Sour Chicken Soup",
        "Chicken Clear Soup",
        "Creamy Chicken Soup",
        "Sweet Corn Veg Soup",
        "Hot & Sour Veg Soup",
        "Cream of Mushroom Soup",
        "Tomato Soup"
    ],

    "Starters & Snack": [
        "Beef Cutlet Balls",
        "Chicken Cutlet Balls",
        "Chicken Nuggets",
        "Chicken Samosa",
        "Veg Samosa",
        "Chicken Balls",
        "Chicken Lollipop",
        "French Fries"
    ],

    "Dosa Live Counter": [
        "Plain Dosa",
        "Masala Dosa",
        "Ghee Roast"
    ],

    "Appam Live Counter": [
        "Appam",
        "Egg Appam"
    ],

    "Live Porotta Counter": [
        "Malabar Porotta",
        "Coin Porotta"
    ],

    "Thattukada Counter": [
        "Live Thattukada Items (As Per Preference)"
    ],

    "Traditional Breads & Staples": [
        "Nool Porotta",
        "Idiyappam",
        "Palappam",
        "Kallappam",
        "Pathiri",
        "Kappa"
    ],

    "Chicken Specialties": [
        "Butter Chicken",
        "Chicken Roast",
        "Chicken Stew",
        "Pepper Chicken"
    ],

    "Mutton Specialties": [
        "Mutton Roast",
        "Mutton Stew"
    ],

    "Duck Specialties": [
        "Duck Roast",
        "Duck Mappas"
    ],

    "Beef Specialties": [
        "Beef Peralan",
        "Beef Chaps",
        "Beef Stew",
        "Beef Roast"
    ],

    "Pork Specialties": [
        "Pork Vindaloo",
        "Pork Roast",
        "Pork Pepper Fry"
    ],

    "Kerala Specials": [
        "Karimeen Pollichathu",
        "Fish Mango Curry",
        "Meen Peera",
        "Beef Ularthiyathu",
        "Nadan Chicken Curry",
        "Prawns Roast",
        "Prawns Masala",
        "Squid Roast (Koonthal Roast)"
    ],

    "Salads": [
        "Green Salad",
        "Russian Salad",
        "Coleslaw Salad",
        "Waldorf Salad",
        "Fruit & Vegetable Salad",
        "Sprout Salad",
        "Pineapple Salad"
    ],

    "Indo-Chinese Dry Items": [
        "Gobi Manchurian",
        "Spicy Chilli Chicken",
        "Chilli Beef"
    ],

    "Noodles": [
        "Vegetable Noodles",
        "Chicken Noodles",
        "Mixed Noodles"
    ],

    "Biriyani": [
        "Mutton Dum Biriyani",
        "Chicken Dum Biriyani",
        "Beef Dum Biriyani",
        "Kappa Biriyani"
    ],

    "Rice Counter": [
        "Neychoru",
        "Vegetable Pulao",
        "Chicken Fried Rice",
        "Vegetable Fried Rice",
        "Egg Fried Rice"
    ],

    "Fish Specials": [
        "Dinner Roll + Fish Moolie",
        "Round Bread + Fish Moolie",
        "Fish Tawa Fry",
        "Kappa & Fish Curry"
    ],

    "Desserts": [
        "Fruit Salad",
        "Cut Fruits",
        "Gulab Jamun"
    ],

    "Cakes": [
        "Black Forest",
        "White Forest",
        "Vancho",
        "Red Velvet",
        "Belgian Chocolate"
    ],

    "Brownies & Mousse": [
        "Classic Chocolate",
        "American Brownie",
        "Chocolate Mousse Cups",
        "Different Varieties of Mousse Cups"
    ],

    "Puddings": [
        "Caramel Pudding",
        "Bread Butter Pudding",
        "Pineapple Pudding",
        "Tender Coconut Pudding",
        "Biscuit Pudding"
    ],

    "Ice Cream": [
        "Vanilla",
        "Chocolate",
        "Strawberry",
        "Butterscotch",
        "Black Currant",
        "Pista",
        "Mango",
        "Tender Coconut",
        "Cassata",
        "Kulfi",
        "American Nuts",
        "Arabian Dates",
        "Belgian Chocolate"
    ],

    "Ice Cream Combos": [
        "Gulab Jamun with Ice Cream",
        "Fruit Salad with Ice Cream",
        "Brownie with Ice Cream",
        "Pudding with Ice Cream"
    ],

    "Midnight Snacks": [
        "Chicken Roll",
        "Beef Roll",
        "Vegetable Roll",
        "Chicken Sandwich",
        "Club Sandwich",
        "Mini Burger",
        "Cutlets"
    ],

    "Tea & Beverage Station": [
        "Traditional Tea",
        "Cardamom Tea",
        "Ginger Tea",
        "Lemon Tea",
        "Mint Tea",
        "Sulaimani",
        "Black Tea",
        "Masala Tea",
        "Coffee",
        "Black Coffee"
    ],

    "Beverages": [
        "Mineral Water Arrangement"
    ]

};

function getAllItems(){

    const all = [];

    Object.values(menuData).forEach(function(items){

        items.forEach(function(item){

            if(!all.includes(item)){
                all.push(item);
            }

        });

    });

    return all;

}


function updateSuggestions(input){

    const row = input.closest(".category-row");

    const category = row.querySelector(".category-input")
        .value
        .trim()
        .toLowerCase();

    const datalist =
        document.getElementById("menu-items");

    datalist.innerHTML = "";

    let items = [];

    Object.keys(menuData).forEach(function(key){

        if(key.toLowerCase() === category){

            items = menuData[key];

        }

    });

    if(items.length === 0){

        items = getAllItems();

    }

   const search = input.value.toLowerCase();

items.forEach(function(item){

    if(item.toLowerCase().startsWith(search)){

        const option = document.createElement("option");

        option.value = item;

        datalist.appendChild(option);

    }

});
}