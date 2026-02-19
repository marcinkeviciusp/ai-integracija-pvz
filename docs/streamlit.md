# Streamlit Documentation

Streamlit is an open-source Python framework that transforms data scripts into shareable web applications with minimal effort. It enables data scientists and developers to create interactive dashboards, data visualization tools, and machine learning apps using pure Python, without requiring frontend development experience. The framework follows a unique execution model where the entire script reruns from top to bottom whenever a user interacts with widgets, making it intuitive to build reactive applications.

The core philosophy of Streamlit is simplicity - you write Python code with Streamlit commands sprinkled in, run it with `streamlit run your_script.py`, and a local web server automatically serves your interactive application in the browser. The framework provides a comprehensive API for displaying text, data, charts, media, input widgets, layout containers, and more, all accessible through the `st` namespace.

## Running Streamlit Apps

Run a Streamlit application from any Python script file or URL.

```bash
# Run a local Python script
streamlit run your_script.py

# Run with custom arguments (arguments after -- are passed to the script)
streamlit run your_script.py -- --data-path /path/to/data

# Run as a Python module (useful for IDE configuration)
python -m streamlit run your_script.py

# Run directly from a URL
streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
```

## st.write

The versatile "Swiss Army knife" function that automatically renders text, data, charts, and other objects based on their type.

```python
import streamlit as st
import pandas as pd

# Display text with markdown support
st.write("Hello, *World!* :sunglasses:")

# Display numbers
st.write(1234)

# Display DataFrames as interactive tables
st.write(pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
}))

# Display multiple arguments
st.write("The value is:", 42, "and the data is:", {"key": "value"})
```

## st.markdown

Display text formatted with Markdown, including colored text, highlights, and emoji support.

```python
import streamlit as st

# Basic markdown formatting
st.markdown("*Streamlit* is **really** ***cool***.")

# Colored text and highlights
st.markdown("""
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.
""")

# Emoji support
st.markdown("Here's a bouquet &mdash; :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# Soft and hard returns
multi = """If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
"""
st.markdown(multi)
```

## st.dataframe

Display a Pandas DataFrame as an interactive, sortable, searchable table.

```python
import streamlit as st
import pandas as pd
import numpy as np

# Basic dataframe display
df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=("col %d" % i for i in range(20))
)
st.dataframe(df)

# With Pandas Styler for highlighting
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)
st.dataframe(dataframe.style.highlight_max(axis=0))
```

## st.line_chart

Create a line chart from data with automatic axis configuration.

```python
import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

df = pd.DataFrame(
    rng(0).standard_normal((20, 3)),
    columns=["a", "b", "c"]
)

st.line_chart(df)
```

## st.bar_chart

Display a bar chart from data with automatic configuration.

```python
import streamlit as st

# Simple bar chart
st.bar_chart({"d6": [1, 5, 2, 6, 2, 1]})
```

## st.map

Display data points on an interactive map.

```python
import streamlit as st
import numpy as np
import pandas as pd

# Generate sample data around San Francisco
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(map_data)
```

## st.button

Display a clickable button widget that returns True when clicked.

```python
import streamlit as st

if st.button("Click me"):
    st.write("Button was clicked!")

# Multiple buttons
if st.button("Primary", type="primary"):
    st.write("Primary button clicked")

if st.button("Secondary"):
    st.write("Secondary button clicked")
```

## st.slider

Create a slider widget for selecting numeric values or ranges.

```python
import streamlit as st
from datetime import time, datetime

# Simple numeric slider
age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm", age, "years old.")

# Range slider
values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)

# Time slider
appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)),
)
st.write("You're scheduled for:", appointment)

# Datetime slider with custom format
start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm"
)
st.write("Start time:", start_time)
```

## st.selectbox

Create a dropdown selection widget.

```python
import streamlit as st

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

st.write("You selected:", option)
```

## st.multiselect

Create a multi-selection dropdown widget.

```python
import streamlit as st

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    default=["Yellow", "Red"],
)

st.write("You selected:", options)
```

## st.checkbox

Create a checkbox widget that returns True when checked.

```python
import streamlit as st
import numpy as np
import pandas as pd

agree = st.checkbox("I agree")
if agree:
    st.write("Great!")

# Use checkbox to toggle content visibility
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c']
    )
    st.dataframe(chart_data)
```

## st.text_input

Create a single-line text input widget.

```python
import streamlit as st

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)

# With key for session state access
st.text_input("Your name", key="name")
st.write("Hello,", st.session_state.name)
```

## st.date_input

Create a date picker widget.

```python
import streamlit as st
import datetime

d = st.date_input("When's your birthday", datetime.date(2020, 8, 11))
st.write("Your birthday is:", d)
```

## st.file_uploader

Create a file upload widget supporting single or multiple files.

```python
import streamlit as st
import pandas as pd

uploaded_files = st.file_uploader(
    "Upload data",
    accept_multiple_files=True,
    type="csv"
)

for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write(df)
```

## st.columns

Create side-by-side columns for layout organization.

```python
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
```

## st.tabs

Create tabbed containers for organizing content.

```python
import streamlit as st

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
```

## st.expander

Create a collapsible container for hiding/showing content.

```python
import streamlit as st

st.bar_chart({"d6": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg", width=200)
```

## st.sidebar

Add widgets and content to a left sidebar panel.

```python
import streamlit as st

# Add widgets to sidebar
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# Main content area
st.write("Main content here")
st.write(f"Contact method: {add_selectbox}")
st.write(f"Selected range: {add_slider}")
```

## st.form

Create a form container that batches widget inputs until submission.

```python
import streamlit as st

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")
```

## st.metric

Display a metric with an optional delta indicator.

```python
import streamlit as st

# Single metric
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

# Multiple metrics in columns
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
```

## st.chat_message and st.chat_input

Build conversational chat interfaces with message containers and input.

```python
import streamlit as st

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
```

## st.session_state

Store and access state that persists across reruns.

```python
import streamlit as st

# Initialize state
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Increment counter
if st.button("Increment"):
    st.session_state.counter += 1

st.write(f"Counter: {st.session_state.counter}")

# Access widget values via key
st.text_input("Your name", key="name")
st.write(f"Hello, {st.session_state.name}")
```

## st.cache_data

Cache the return value of data-fetching functions to improve performance.

```python
import streamlit as st

@st.cache_data
def load_data(url):
    # This expensive operation only runs once per unique URL
    import pandas as pd
    return pd.read_csv(url)

@st.cache_data
def square(x):
    return x**2

@st.cache_data
def cube(x):
    return x**3

# Clear all cached data
if st.button("Clear All"):
    st.cache_data.clear()

# Use cached functions
data = load_data("https://example.com/data.csv")
st.write(f"5 squared is {square(5)}")
st.write(f"3 cubed is {cube(3)}")
```

## st.progress

Display a progress bar for long-running operations.

```python
import streamlit as st
import time

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)

time.sleep(1)
my_bar.empty()

st.button("Rerun")
```

## st.spinner

Display a spinner during long-running operations.

```python
import streamlit as st
import time

with st.spinner("Wait for it...", show_time=True):
    time.sleep(5)

st.success("Done!")
```

## st.status

Display a status container that can expand to show operation details.

```python
import streamlit as st
import time

with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)

st.button("Rerun")
```

## st.dialog

Create modal dialog popups using a decorator.

```python
import streamlit as st

@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    st.write(f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}")
```

## st.fragment

Create a fragment that can rerun independently without rerunning the full app.

```python
import streamlit as st

if "app_runs" not in st.session_state:
    st.session_state.app_runs = 0
    st.session_state.fragment_runs = 0

@st.fragment
def fragment():
    st.session_state.fragment_runs += 1
    st.button("Rerun fragment")
    st.write(f"Fragment says it ran {st.session_state.fragment_runs} times.")

st.session_state.app_runs += 1
fragment()
st.button("Rerun full app")
st.write(f"Full app says it ran {st.session_state.app_runs} times.")
st.write(f"Full app sees that fragment ran {st.session_state.fragment_runs} times.")
```

## st.navigation

Configure multipage app navigation with pages defined as files or functions.

```python
import streamlit as st

def page_2():
    st.title("Page 2")

# Navigate between a file-based page and a function-based page
pg = st.navigation(["page_1.py", page_2])
pg.run()
```

## Configuration (config.toml)

Configure Streamlit behavior and theming via `.streamlit/config.toml`.

```toml
[server]
port = 8501
headless = true

[theme]
primaryColor = "#F63366"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[browser]
gatherUsageStats = false
```

## Secrets Management (secrets.toml)

Store sensitive configuration in `.streamlit/secrets.toml` for secure access.

```toml
# .streamlit/secrets.toml
db_username = "admin"
db_password = "supersecret123"

[database]
host = "localhost"
port = 5432
```

```python
import streamlit as st

# Access secrets in your app
username = st.secrets["db_username"]
password = st.secrets["db_password"]
db_host = st.secrets["database"]["host"]
```

Streamlit is primarily designed for building data exploration tools, machine learning model demos, internal dashboards, and rapid prototyping of data-driven applications. Common use cases include visualizing datasets with interactive filters, building chatbot interfaces for LLM applications, creating model evaluation dashboards, and developing quick proof-of-concept apps that can be shared with stakeholders.

Integration patterns typically involve combining Streamlit with data processing libraries like Pandas and NumPy, visualization libraries like Altair and Plotly, machine learning frameworks like scikit-learn and PyTorch, and database connections through the `st.connection` API. For production deployments, apps can be hosted on Streamlit Community Cloud for free, deployed to cloud platforms via Docker containers, or integrated into enterprise environments using Kubernetes. The framework's caching mechanisms (`@st.cache_data` and `@st.cache_resource`) enable efficient handling of expensive computations and database queries, while session state management allows building complex multi-step workflows and maintaining user context across interactions.
