III. Sidebar and Layout
This section demonstrates how to design a user-friendly and organized layout in a Streamlit application. The example focuses on Data Warehousing and Enterprise Data Management (EDM)—two essential concepts in large-scale data systems.
The sidebar, created using st.sidebar, acts as a control panel where users can select different topics from a dropdown (st.selectbox) and optionally display a glossary using a checkbox. This design pattern keeps the main page clean while allowing users to easily navigate or modify the view.
To better separate content, the app uses st.tabs() to create two logical sections:
Theory: Contains educational information about data warehousing concepts.
Real-World Use: Provides industry-specific use cases (e.g., retail and healthcare) presented side-by-side using st.columns().
An additional layout component, st.expander(), is used within the Theory tab. It hides in-depth information on Data Governance, which users can optionally expand to read more—supporting a cleaner and more interactive user experience.

Lastly, if the user enables the "Show Glossary" option from the sidebar, Streamlit displays a glossary of relevant terms such as ETL, EDM, OLAP, and Data Mart. This is especially useful for beginners or viewers unfamiliar with technical terms.
![image](https://github.com/user-attachments/assets/67edb077-6a07-4741-9e0b-29d9d000aa58)

![image](https://github.com/user-attachments/assets/2c812e86-2261-4d53-805d-ef7f7a09ff50)
![image](https://github.com/user-attachments/assets/86c13346-bfb3-4d7c-811e-1f0485be14fb)

