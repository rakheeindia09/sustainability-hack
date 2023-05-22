Demo Video googledrive Link -- https://drive.google.com/drive/folders/1w8gGC21cv7-8qZnlyzCPRingVXlTaNds

The idea is to have electric roads as escalators using solar energy which would help reduce air pollution to a great extent which will also reduce the cost of building roads every time helping the government public sector domain. Hopefully Once the air pollution is reduced slowly the climatic conditions will get back to it's normal state with respect to summer, rainy, winter seasons which as of now has changed a lot.

Hackathon submission To have smart energy management for electric roads using solar energy to charge vehicles, while incorporating Azure and MSM (Microsoft Smart Energy Management), we follow these steps for our project:

Solar Energy Generation: Install solar panels along the electric roads to generate renewable energy. Ensure the panels are positioned optimally for maximum sunlight exposure.

Energy Storage: Set up energy storage systems, such as batteries, to store excess energy generated during the day. This stored energy can be used during low solar generation periods or during high demand.

Smart Metering: Implement smart metering infrastructure to monitor energy consumption and generation in real-time. Smart meters can provide data on individual vehicle charging, road energy usage, and overall energy flows.

Data Collection and Analysis: Connect the smart metering infrastructure to Azure IoT (Internet of Things) Hub. This allows for the collection and analysis of energy data from various sources, including solar generation, battery storage, and vehicle charging.

Azure IoT Suite: Utilize Azure IoT Suite, which offers a range of services for building and managing IoT applications. Leverage Azure IoT Hub, Azure Stream Analytics, and Azure Machine Learning to process and analyze the collected energy data.

Energy Demand Prediction: Used historical and real-time data to develop predictive models like LSTM, Linear regression and light GBM model that forecast energy demand for vehicle charging. Azure Machine Learning helped create accurate demand prediction models based on factors like traffic patterns, weather conditions, and historical usage.

Energy Management Algorithms: Develop energy management algorithms that optimize the energy distribution and charging schedules based on demand predictions and available solar energy. These algorithms can determine the most efficient use of stored energy and prioritize charging for vehicles with immediate needs. Used function app for this from Azure and set energy consumption as a threshold. Also used gradio library for web deployment.

Vehicle-to-Grid Integration: Implement Vehicle-to-Grid (V2G) technology, which allows electric vehicles to discharge excess energy back into the grid when not in use. This feature helps stabilize the grid and provide additional power during peak demand periods.

Integration with Microsoft Smart Energy Management: Utilize Microsoft Smart Energy Management (MSM) solutions to integrate with the energy management system. MSM offers additional features like for calculating cost of energy consumed, real-time monitoring, and energy optimization algorithms and reduction/sustainability goals.

Feedback and Iteration: Continuously monitor the system's performance and gather feedback to refine the algorithms and improve energy management efficiency. Use the insights gained from data analysis to optimize charging schedules, maximize solar energy utilization, and enhance overall energy management.

By implementing these steps, we created a smart energy management system for electric roads that efficiently utilizes solar energy, incorporates Azure's powerful data analysis capabilities, and integrates with Microsoft Smart Energy Management for enhanced features and optimization.

