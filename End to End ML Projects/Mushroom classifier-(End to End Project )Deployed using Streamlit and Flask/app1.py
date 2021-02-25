
import pickle
import streamlit as st
model=pickle.load(open('decisiontree.pkl','rb'))


def mushroom(gill_color,ring_type,gill_size,bruises,stalk_root,gill_spacing,habitat,spore_print_color,population):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: gill_color
        in: query
        type: number
        required: true
      - name:ring_type
        in: query
        type: number
        required: true
      - name: gill_size
        in: query
        type: number
        required: true
      - name: bruises
        in: query
        type: number
        required: true
      - name: stalk_root
        in: query
        type: number
        required: true
      - name: gill_spacing
        in: query
        type: number
        required: true
      - name: habitat
        in: query
        type: number
        required: true
      - name:spore_print_color
        in: query
        type: number
        required: true
      - name:population
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    prediction=model.predict([[gill_color,ring_type,gill_size,bruises,stalk_root,gill_spacing,habitat,spore_print_color,population]])
    print(prediction)
    return prediction
    

def main():
        html_temp="""
                     
    
        <div style="background-color:tomato;padding:10px">
        <h2 >Streamlit Mushroom Classifier </h2>

        """
        #To use the html file we use maekdown
        st.markdown(html_temp,unsafe_allow_html=True)
    
        gill_color=st.text_input("Gill-color","Type Here Eg:1")
        ring_type=st.text_input('Ring-type',"Type Here Eg:1" )
        gill_size=st.text_input('Gill-size',"Type Here Eg:0")
        bruises=st.text_input('Bruises',"Type Here Eg:4")
        stalk_root=st.text_input('Stalk-root',"Type Here Eg:0")
        gill_spacing=st.text_input('Gill-spacing',"Type Here Eg:1")
        habitat=st.text_input('Habitat',"Type Here Eg:3")
        spore_print_color=st.text_input('Spore-print-color',"Type Here Ex:4")
        population=st.text_input('Population',"Type Here Eg:2")
        result=""
        if st.button("Predict"):
            result=mushroom(gill_color,ring_type,gill_size,bruises,stalk_root,gill_spacing,habitat,spore_print_color,population)
        st.success("The mushroom type is {}".format(result))

if __name__=='__main__':
    main()
    
    