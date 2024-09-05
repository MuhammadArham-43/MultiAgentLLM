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

### Query: How To Bake a cake at home with minimal ingredients

<details>
    <summary>Expand to view response</summary>
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
