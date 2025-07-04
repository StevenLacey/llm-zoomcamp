     /project_root
     ├── /src
     │   ├── __init__.py
     │   ├── main.py  # Entry point for your application
     │   ├── /data
     │   │   ├── data_loader.py  # Functions for loading data
     │   │   ├── data_saver.py  # Functions for saving data
     │   ├── /models
     │   │   ├── user.py  # User-related classes and functions
     │   │   ├── conversation.py  # Conversation-related classes and functions
     │   ├── /services
     │   │   ├── llm_service.py  # Functions for interacting with the LLM
     │   │   ├── elasticsearch_service.py  # Functions for Elasticsearch interactions
     │   ├── /utils
     │   │   ├── helpers.py  # General utility functions
     ├── /notebooks
     │   ├── 01b_intake_greeting.ipynb
     │   ├── 02b_initial_conversations.ipynb
     │   ├── 03_rag_prompt_with_elasticsearch_v1.1.ipynb
     │   ├── 04_other_notebook.ipynb
     ├── /context  # Keep your context files here
     ├── requirements.txt
     └── README.md