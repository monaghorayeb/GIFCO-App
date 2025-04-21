import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="GIFCO Logistics", layout="wide")

# Sidebar navigation
page = st.sidebar.radio(
    " ",
    ["Home", "KPI Dashboard", "Forecast Dashboard"]
)

# Home Page
if page == "Home":
    st.image("logo.png", width=150)
    st.markdown("""
      <h1 style="text-align: center;">✈️ GIFCO Logistics & Freight Services 🚢</h1>
    """, unsafe_allow_html=True)

    st.header("🌍 About GIFCO")
    st.markdown("""
    GIFCO is a leading logistics and freight company based in **Lebanon**, providing seamless services for the movement of goods across the globe.

    They are known for:
    - A strong **network** connecting key global trade routes  
    - Comprehensive **freight management** from port to destination  
    - Handling **air, sea, and land** freight services  
    - Expertise in **customs clearance** and supply chain optimization  
    """)

    st.image("logistics_image.png", caption="GIFCO logistics achievements over the years", use_column_width=True)

    st.markdown("""
    GIFCO is a member of the following accredited logistic networks:  
    """)

    st.image("networks.png", caption="GIFCO logistics achievements over the years", use_column_width=True)

    st.header("📦 GIFCO Services")
    st.markdown("""
    GIFCO offers a wide range of logistics services, including:
    - **Freight forwarding** across global trade lanes
    - **Warehousing and inventory management**  
    - **Customs clearance and documentation**  
    - **Real-time shipment tracking** to enhance transparency and customer satisfaction  
    """)


# KPI Dashboard
elif page == "KPI Dashboard":
    st.title("📊 GIFCO KPI Dashboard")
    st.markdown("Explore the live KPIs and product insights below:")

    components.iframe(
    "https://public.tableau.com/views/GIFCODashboard/Dashboard1?:embed=y&:display_count=yes&:showVizHome=no",
    height=1200,
    width=1600
    )
    

# Forecast Dashboard
elif page == "Forecast Dashboard":
    st.title("📈 GIFCO Forecast Dashboard")
    st.markdown("This section shows forecasted sales trends generated using the Theta Model.")

    st.image("BestModel.png", caption="6-years Theta Forecast", use_column_width=True)

    st.markdown("""
    ### 🔍 Insights:
    - **Sales Forecast Overview**: The Theta model projects significant sales growth from 2025 to 2030, indicating rising demand and a strong market expansion post-2024. This forecast reflects the company’s growth potential and offers a roadmap for scaling operations to meet future needs.
    - **Data-Driven Growth**: Based on historical data patterns, this forecast suggests a steady upward trajectory, supporting the need for increased investment in production capacity, logistics, and infrastructure. The consistency of the growth trend underscores the long-term sustainability of GIFCO’s business model.
    - **Strategic Planning**: The forecast should guide strategic decisions regarding capital allocation. This includes expanding production capacity, optimizing inventory management, and scaling distribution networks to accommodate increasing demand, particularly starting in 2025.
    - **Investment in Key Areas**: The rising sales projections highlight the importance of investing in service expansion, particularly in high-growth markets like Egypt and UAE. Increasing capacity in storage and warehousing will also be essential to meet future demand.
    - **Market Expansion and Diversification**: As sales are expected to grow, there are significant opportunities for market expansion. Targeting new geographic regions and diversifying into additional service offerings, such as air freight or premium storage solutions, will be key to sustaining growth.
    - **Potential Risks and Monitoring**: While the forecast is based on stable historical trends, external factors such as economic downturns, regional instability, or global trade disruptions could impact the accuracy of predictions. Ongoing monitoring and adjustments to the forecast will be crucial to remain responsive to market shifts.
    - **Long-Term Strategy**: The forecast points to a consistent and reliable growth pattern. However, as forecasting accuracy may decline over time due to increasing uncertainties, maintaining operational flexibility will be essential to adapt to future market dynamics.
    - **Actionable Insights**: The data supports increased infrastructure development to meet projected demand, particularly as 2025 approaches. A focus on expanding production and distribution networks will position the company to lead in its key markets.
    
    **Note: The forecast is based on historical trends and seasonal behavior; real-world deviations can occur, especially in volatile markets.**
    """)