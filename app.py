import streamlit as st
import os
# Import GPT4-Vision model (Assuming you have a module or API for GPT4-Vision)
from GPT4VisionModel import GPT4ImageOptimizer

# Define Streamlit app layout
st.title('Landing Page Optimizer with GPT4-Vision')
st.sidebar.title('Settings')
api_key = st.sidebar.text_input("Enter API KEY:", type="password")
# Upload landing page image
count = 0
uploaded_image = st.sidebar.file_uploader('Upload Landing Page Image', type=['jpg', 'png'],key=count)
count += 1

# Initialize GPT4ImageOptimizer
optimizer = GPT4ImageOptimizer(api_key)


# Upload landing page image
uploaded_image = st.sidebar.file_uploader('Upload Landing Page Image', type=['jpg', 'png'])

if uploaded_image:
    # Display uploaded image
    st.image(uploaded_image, caption='Uploaded Landing Page Image', use_column_width=True)
    
    temp_image_path = os.path.join(os.getcwd(), "temp_image.jpg")
    with open(temp_image_path, "wb") as temp_file:
        temp_file.write(uploaded_image.read())

    with st.spinner("We are analyzing your landing page image..."):
        visual_prompt = """
        - Evaluate the visual hierarchy of the landing page. Are the most important elements, such as the main headline,
        key benefits, and call-to-action, given appropriate prominence? Assess if the visual hierarchy guides the user's attention 
        in the desired order. 
        Provide recommendations on how to improve the visual hierarchy through the use of size, color, contrast, and placement.
        """
        
        # Analyze image using GPT4-Vision
        st.subheader('1. Visual Hierarchy:')
        optimization_result = optimizer.optimize_landing_page(temp_image_path,visual_prompt)
        st.write(optimization_result)
        
        color_prompt = """
        - Analyze the color scheme used on the landing page. Does it align with the brand's identity and evoke the desired emotions? 
        Evaluate if the colors are harmonious, visually appealing, and contribute to the overall aesthetic. 
        Suggest improvements to the color palette, 
        such as using complementary or contrasting colors, to enhance the visual impact and reinforce the message.
        """
        st.subheader('2. Color Evaluation')
        optimization_result = optimizer.optimize_landing_page(temp_image_path,color_prompt)
        st.write(optimization_result)
        
        illustration_prompt = """
        - Assess the use of icons and illustrations on the landing page. 
        Do they enhance the visual communication and make the content more engaging? Evaluate if the icons and illustrations are consistent 
        in style, relevant to the content, and add value to the user experience. 
        Provide feedback on the selection, sizing, and placement of icons and illustrations to maximize their effectiveness."""
        # A/B Testing Guidance section (You'll need to implement this based on your requirements)
        st.subheader('3. Iconography and Illustrations')
        optimization_result = optimizer.optimize_landing_page(temp_image_path,illustration_prompt)
        st.write(optimization_result)

        white_space_prompt ="""
        - Examine the use of whitespace (or negative space) on the landing page. Is it effectively utilized to create visual breathing room
        and improve readability? Assess if the whitespace balances the content, separates sections, and provides a clean and uncluttered look. 
        Offer suggestions on optimizing the whitespace to enhance the overall design and user experience.
        """

        # Performance Tracking section (You'll need to implement this based on your requirements)
        st.subheader('4. Whitespace Utilization')
        optimization_result = optimizer.optimize_landing_page(temp_image_path,white_space_prompt)
        st.write(optimization_result)

        branding_prompt ="""
        -  Evaluate the consistency of design elements across the landing page. 
        Are the typography, colors, button styles, and other visual components used consistently throughout? 
        Assess if the design aligns with the brand's guidelines and creates a cohesive and recognizable experience. 
        Provide recommendations on maintaining consistency and strengthening the brand presence.
        """

        # Performance Tracking section (You'll need to implement this based on your requirements)
        st.subheader('5. Consistency and Branding')
        optimization_result = optimizer.optimize_landing_page(temp_image_path,branding_prompt)
        st.write(optimization_result)

        imagery_prompt ="""
        - Analyze the quality and relevance of images and videos used on the landing page.
        Do they effectively showcase the product, service, or concept being promoted? 
        Evaluate if the visuals are high-resolution, visually appealing, and contribute to the overall message.
        Suggest improvements to the selection and placement of images and videos to maximize their impact and engagement.
        """

        # Performance Tracking section (You'll need to implement this based on your requirements)
        st.subheader('6. Imagery and Video')
        optimization_result = optimizer.optimize_landing_page(temp_image_path,imagery_prompt)
        st.write(optimization_result)

        imagery_prompt ="""
        - Analyze the quality and relevance of images and videos used on the landing page.
        Do they effectively showcase the product, service, or concept being promoted? 
        Evaluate if the visuals are high-resolution, visually appealing, and contribute to the overall message.
        Suggest improvements to the selection and placement of images and videos to maximize their impact and engagement.
        """

        # Performance Tracking section (You'll need to implement this based on your requirements)
        st.subheader('6. Imagery and Video')
        optimization_result = optimizer.optimize_landing_page(temp_image_path,imagery_prompt)
        st.write(optimization_result)

        design_prompt ="""
        - Assess the design and usability of any forms present on the landing page, such as contact forms or signup forms.
        Are the form fields clearly labeled, intuitively arranged, and easy to complete? 
        Evaluate if the form design is visually appealing, aligns with the overall page design, and minimizes friction for the user. 
        Provide suggestions on optimizing the form design to improve completion rates and user experience.
        """

        # Performance Tracking section (You'll need to implement this based on your requirements)
        st.subheader('7. Form Design')
        optimization_result = optimizer.optimize_landing_page(temp_image_path,design_prompt)
        st.write(optimization_result)

        responsive_prompt ="""
        - Test the landing page on various mobile devices to assess its responsiveness and mobile-friendliness. 
        Evaluate if the design adapts seamlessly to different screen sizes, maintaining readability, usability, and visual appeal. 
        Identify any issues with touch targets, text legibility, or content hierarchy on mobile devices. 
        Provide recommendations on optimizing the mobile experience to ensure a smooth and engaging interaction.
        """

        # Performance Tracking section (You'll need to implement this based on your requirements)
        st.subheader('8. Mobile Responsiveness')
        optimization_result = optimizer.optimize_landing_page(temp_image_path,responsive_prompt)
        st.write(optimization_result)

        performance_prompt ="""
        - Analyze the loading speed and performance of the landing page. 
        Does it load quickly, even with visuals and interactive elements? 
        Evaluate if there are any performance bottlenecks, such as large image files or unoptimized code, that impact the page's loading time. 
        Suggest optimizations to improve the loading speed, such as image compression, lazy loading, or code minification, 
        to provide a fast and seamless user experience.
        """

        # Performance Tracking section (You'll need to implement this based on your requirements)
        st.subheader('9. Loading Speed and Performance')
        optimization_result = optimizer.optimize_landing_page(temp_image_path,performance_prompt)
        st.write(optimization_result)

        accessibility_prompt ="""
        - Assess the accessibility of the landing page design. 
        Is it usable and understandable for users with different abilities and disabilities? 
        Evaluate if the page follows accessibility best practices, such as providing alternative text for images, 
        sufficient color contrast, and keyboard navigation support. Identify any accessibility barriers and provide 
        recommendations on making the design more inclusive and compliant with accessibility guidelines.
        """

        # Performance Tracking section (You'll need to implement this based on your requirements)
        st.subheader('10. Accessibility')
        optimization_result = optimizer.optimize_landing_page(temp_image_path,accessibility_prompt)
        st.write(optimization_result)

# Footer
st.markdown("""
    *Powered by GPT4-Vision - Developed by KeenSight*
""")
