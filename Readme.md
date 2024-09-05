# Multi-Agent LLM with Real-Time Search Capabilities

_Author: Muhammad Arham_

<p>This repository uses CrewAI multi-agentic capabilites and combines them with real-time internet and youtube search to provide a general-purpose LLM. It fetches up-to-date information using YouTubeDataAPI and Traversaal's ARES API to answer user's query in the best possible manner.
</p>

## Setup

1. Install Ollama if you want to use a locally-served LLM. Download and install from the official package available on their <a href="https://ollama.com/">website.</a>
2. Create a .env file and add the required API Keys and URLs following the provided .env.example file. The package requires API Keys for YouTubeDataAPIv3 and Traversaal's Ares API.
3. A simple bash file is provided that creates a Python environment and sets up the FastAPI backend and the streamlit-based frontend.

```
bash runfile.sh
```

## Implementation Details

We use <a href="https://docs.crewai.com/">CrewAI</a> as our agentic-framework that comprises of three simple parts. The framework is summarized in the image below:<br>
<img src="assets/flowchart.png" alt="Multi-agent Framework Flowchart"></img>
<br>

### Choice of LLM

The implementation currently supports Ollama and Cohere as LLM providers.
The primary choice is Llama3.1-8B served locally using Ollama due to its state-of-the-art performance on multi-purpose tasks, and multi-modal capabilties.
<br>Nonetheless, given memory constraints and RAM issues, hosting a LLM locally can be a challenge. Cohere API can be used as an external source for LLM responses that aleviates the constraints.

## Sample Responses

<details>
    <summary>How To Bake a cake at home with minimal ingredients</summary>
    Baking a Simple Cake at Home: A Step-by-Step Guide
1. Introduction

Welcome to the world of home baking! In this guide, we'll show you how to create a delicious and simple cake using everyday ingredients. Whether you're a beginner or an experienced baker, this recipe is a great way to enjoy a homemade treat without any complexity. 2. Ingredients and Their Quantities

For this recipe, you will need the following:

    2 cups (240g) of all-purpose flour: The base of your cake, providing structure and texture.
    1 teaspoon baking powder: A leavening agent to help the cake rise.
    1/2 teaspoon baking soda: Another leavening agent for a lighter texture.
    1/2 cup (100g) granulated sugar: Sweetens the cake and adds a delightful crunch.
    2 large eggs: Binding agent and contributes to the cake's structure.
    1/2 cup (120ml) vegetable oil: Moisturizes the cake and ensures a tender crumb.
    1 cup (240ml) milk: Provides moisture and helps combine the ingredients.
    1 teaspoon vanilla extract: Adds a classic, sweet flavor.

3. Step-by-Step Baking Instructions

    Preheat and Prepare: Start by preheating your oven to 350°F (180°C). Grease and flour a 9-inch (23 cm) round cake pan to prevent sticking.
    Mix Dry Ingredients: In a large mixing bowl, combine the flour, baking powder, and baking soda. Whisk until well blended.
    Combine Wet Ingredients: In a separate bowl, whisk together the sugar, eggs, oil, milk, and vanilla extract. Mix until you have a smooth, uniform consistency.
    Combine and Mix: Slowly pour the wet ingredients into the dry ingredients, stirring as you go. Mix until you achieve a smooth batter, being careful not to overmix.
    Bake: Pour the batter into the prepared cake pan and smooth the top. Bake for 30-35 minutes. The cake is done when a toothpick inserted into the center comes out clean.
    Cool and Enjoy: Let the cake cool in the pan for a few minutes, then transfer to a wire rack to cool completely. Serve and enjoy!

4. Baking Tips and Tricks

    Temperature Matters: Preheat your oven accurately and use room temperature ingredients for the best results. This ensures even baking and a consistent texture.
    Avoid Overmixing: Overmixing can lead to a tough cake. Mix until the ingredients are combined, but don't overdo it.
    Test for Doneness: Always use a toothpick to check if your cake is baked through. Insert it into the center, and if it comes out clean, your cake is ready!

5. Variations and Creative Ideas

    Flavor Boost: Add a pinch of salt to enhance the overall flavor.
    Flavor Twists: Experiment with different extracts like almond or lemon for a unique taste experience.
    Texture Add-Ins: Fold in chopped nuts or chocolate chips for a delightful crunch and extra flavor.
    Serving Suggestions: Dust with powdered sugar or top with whipped cream for a simple yet elegant presentation.

6. Conclusion

Baking a simple cake at home is an enjoyable and accessible activity. With this guide, you can create a delicious treat with minimal ingredients and effort. Remember, baking is an art, and with practice, you can master it. Enjoy your homemade cake and the satisfaction of creating something special!

Happy baking, and may your kitchen be filled with the aroma of freshly baked goodness!

</details>

<details>
    <summary>Prepare a presentation deck on the basics on Regression methods</summary>
Basics of Regression Methods
Introduction

Regression analysis is a fundamental statistical technique used to understand and predict relationships between variables. It is a powerful tool for data scientists and analysts, offering insights into various real-world scenarios.
Understanding Regression
Definition

Regression is a statistical method to model the relationship between a dependent variable (target) and one or more independent variables (predictors). The goal is to estimate the impact of changes in the independent variables on the dependent variable.
Types of Regression Methods

    Simple Regression:
        This method focuses on the relationship between a single dependent and independent variable.
        Use Case: Analyzing basic relationships, e.g., sales revenue as a function of advertising spend.

    Multiple Regression:
        Multiple regression extends the analysis to include multiple independent variables.
        Application: Predicting house prices based on factors like location, size, and age.

    Linear Regression:
        Assumes a linear relationship between variables, represented by a straight line.
        Ideal for simple scenarios where the relationship is linear.

    Multiple Linear Regression:
        Combines multiple independent variables with a linear relationship.
        Use: Predicting outcomes influenced by multiple factors, e.g., student performance based on study hours and class attendance.

    Logistic Regression:
        Suitable for categorical or binary dependent variables.
        Predicts probabilities, e.g., whether a customer will churn or not.

    Ridge and Lasso Regression:
        Ridge and Lasso are regularization techniques for multiple regression.
        Ridge regression handles multicollinearity by adding a degree of bias.
        Lasso regression performs feature selection by shrinking less important coefficients to zero.

    Polynomial Regression:
        Models non-linear relationships by adding higher-order terms to the equation.
        Useful when the relationship is not linear.

Choosing the Right Regression Method

    Simple vs. Multiple: The choice depends on the number of independent variables. Simple regression is for single-variable analysis, while multiple regression handles multiple predictors.
    Linear vs. Non-Linear: Linear regression is suitable for linear relationships, while polynomial regression captures non-linear patterns.
    Regularization: Ridge and Lasso regression are used to address issues like multicollinearity and feature selection in multiple regression models.

Conclusion

Regression methods are essential in data analysis and predictive modeling. Understanding the various types and their applications is key to effective model building. Further exploration can lead to advanced techniques, such as machine learning algorithms, and practical applications in various fields.
References

    Indeed
    Analytics Vidhya
    GeeksforGeeks

This presentation offers a concise overview of regression methods. For a comprehensive understanding, further study, including practical examples and mathematical formulations, is recommended.

</details>

<details>
    <summary>I need to buy a new phone within the budget of 400 USD. Explore reviews online and suggest me possible options and where to buy them</summary>
Phone Recommendations Under $400
1. Introduction

If you're in the market for a new smartphone and have set a budget of $400, you're in luck! This price range offers a variety of options that combine affordability with impressive features. In this guide, we'll explore some of the top choices available, helping you make an informed decision. 2. Budget-Friendly Options
Samsung Galaxy A14

The Samsung Galaxy A14 is a highly sought-after device in this category. It boasts a 6.6-inch HD+ display, providing a spacious viewing experience. The 50MP main camera captures stunning images, and the 5000mAh battery ensures you can use your phone all day without worrying about running out of power. It runs on the latest Android 13 OS and comes in various colors to suit your style.
Google Pixel 6a

Google's Pixel 6a is another excellent choice for those seeking a balance between performance and affordability. It features a 6.1-inch FHD+ display, delivering crisp visuals. The 12MP dual-pixel rear camera is renowned for its exceptional image quality, and the 4410mAh battery keeps the phone running smoothly throughout the day. The Pixel 6a runs on Android 12 and offers a seamless user experience.
Motorola Moto G Stylus 5G

For those seeking a unique feature, the Motorola Moto G Stylus 5G is a standout option. It comes with a built-in stylus, perfect for creative professionals and note-takers. The 6.8-inch FHD+ display provides ample screen real estate, and the 50MP main camera captures detailed photos. The 5000mAh battery ensures you can use the stylus for extended periods without worrying about battery life. 3. Key Features and Specifications
Model Display Camera Battery Storage
Samsung Galaxy A14 6.6-inch HD+ 50MP main camera 5000mAh 64GB/128GB
Google Pixel 6a 6.1-inch FHD+ 12MP dual-pixel 4410mAh 128GB
Motorola Moto G Stylus 5G 6.8-inch FHD+ 50MP main camera 5000mAh 128GB 4. Online Reviews and Ratings

These phones have garnered positive feedback from reputable sources:

    Samsung Galaxy A14: TechRadar applauds its battery life and vibrant display, while Android Central praises its performance and camera.
    Google Pixel 6a: Trusted Reviews and Android Authority commend its camera quality and value, respectively.
    Moto G Stylus 5G: CNET and PCMag highlight its display, stylus, performance, and battery life.

5. Where to Buy

You can purchase these phones from popular online retailers like Amazon, Best Buy, and the official brand websites. Additionally, carrier stores such as Verizon, AT&T, and T-Mobile often offer deals and promotions, making them worth exploring. 6. Conclusion
With a $400 budget, you have access to a diverse range of high-quality smartphones. The Samsung Galaxy A14, Google Pixel 6a, and Motorola Moto G Stylus 5G excel in performance, features, and value. Online reviews validate their strengths, and you can conveniently buy them from various sources. Remember to consider your specific needs and preferences when making your decision. Happy shopping, and enjoy your new smartphone!

</details>
