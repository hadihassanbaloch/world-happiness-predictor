import pandas as pd
import streamlit as st
import joblib 

model = joblib.load('world_happiness_model.pkl')

def predict_happiness(gdp, social_support, health_life_expectancy,freedom, 
                      generosity, corruption, positive_effect, negative_effect):
    # Prepare input data as a DataFrame
    input_data = pd.DataFrame({
        'year': [2023],
        'Log GDP per capita': [gdp],
        'Social support': [social_support],
        'Healthy life expectancy at birth': [health_life_expectancy],
        'Freedom to make life choices': [freedom],  # You can set default values for other columns
        'Generosity': [generosity],
        'Perceptions of corruption': [corruption],
        'Positive affect': [positive_effect],
        'Negative affect': [negative_effect] 
    })

    # Make prediction
    happiness_score = model.predict(input_data)
    return happiness_score[0]

def main():
    st.title('World Happiness Predictor')
    st.write('This app predicts the Happiness Score (Life Ladder) for a country based on various factors. The Happiness Score ranges from 0 to 10, where higher values indicate greater happiness and well-being.')

    st.write('### Enter the values to predict the Happiness Score:')

    st.write('#### Log GDP per capita:')
    st.write('''GDP per capita is a measure of a country’s economic output that accounts for its number of people.
             It is adjusted for inflation and converted to logarithmic scale.''')
    gdp = st.number_input('Log GDP per capita', format="%.2f", step=0.01)

    st.write('#### Social Support:')
    st.write('Social support indicates the perceived quality of social connections and the availability of help when needed.')
    social_support = st.slider('Social Support', min_value=0.0, max_value=2.0, step=0.01)

    st.write('#### Healthy Life Expectancy at Birth:')
    st.write('This is the average number of years a newborn is expected to live in good health.')
    health_life_expectancy = st.slider('Healthy life expectancy at birth', min_value=0.0, max_value=100.0, step=0.1)
    
    # Additional sliders for other features with brief explanations
    st.write('#### Freedom to Make Life Choices:')
    st.write('This measures the perceived freedom of choice in life decisions.')
    freedom = st.slider('Freedom to make life choices', min_value=0.0, max_value=1.0, step=0.01)

    st.write('#### Generosity:')
    st.write('This measures the amount of money donated to charity.')
    generosity = st.slider('Generosity', min_value=0.0, max_value=1.0, step=0.01)

    st.write('#### Perceptions of Corruption:')
    st.write('This measures the level of corruption in a country.')
    corruption = st.slider('Perceptions of corruption', min_value=0.0, max_value=1.0, step=0.01)

    st.write('#### Positive Affect:')
    st.write('This measures the frequency of positive emotions.')
    positive_effect = st.slider('Positive affect', min_value=0.0, max_value=1.0, step=0.01)

    st.write('#### Negative Affect:')
    st.write('This measures the frequency of negative emotions.')
    negative_effect = st.slider('Negative affect', min_value=0.0, max_value=1.0, step=0.01)

    # Predict button
    if st.button('Predict'):
        happiness_prediction = predict_happiness(gdp, social_support, health_life_expectancy,freedom,
                                                 generosity, corruption,positive_effect,negative_effect )
        st.success(f'Predicted Happiness Score: {happiness_prediction:.2f}')
        
        # Visualize the score with a progress bar
        st.progress(happiness_prediction / 10)

        # Provide context on average global happiness
        global_avg_happiness = 5.5  # Example value, adjust based on actual data
        st.write(f'The predicted happiness score is {happiness_prediction:.2f} on a scale of 0 to 10.')
        st.write(f'The average global happiness score is approximately {global_avg_happiness}.')
# Execute the app
if __name__ == '__main__':
    main()