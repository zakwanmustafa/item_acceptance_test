import streamlit as st
from datetime import date, time

# In-memory data store to simulate Firebase Firestore
if 'items' not in st.session_state:
    st.session_state.items = []

# Helper function to reset form inputs
def reset_form():
    st.session_state['itemName'] = ''
    st.session_state['itemType'] = ''
    st.session_state['manufacturer'] = ''
    st.session_state['lotNumber'] = ''
    st.session_state['expiryDate'] = None
    st.session_state['receptionDate'] = None
    st.session_state['receptionTime'] = None
    st.session_state['conditionCheck'] = ''
    st.session_state['performanceCriteria'] = ''
    st.session_state['performanceResult'] = ''
    st.session_state['notes'] = ''
    st.session_state['receivedBy'] = ''
    st.session_state['userName'] = ''
    st.session_state['performedBy'] = ''
    st.session_state['approvedBy'] = ''

st.title("Laboratory Inventory & Performance Tracker")

with st.form(key='item_form'):
    itemName = st.text_input("Item Name", key='itemName')
    itemType = st.text_input("Item Type", key='itemType')
    manufacturer = st.text_input("Manufacturer", key='manufacturer')
    lotNumber = st.text_input("Lot Number", key='lotNumber')
    expiryDate = st.date_input("Expiry Date", key='expiryDate', value=None)
    receptionDate = st.date_input("Reception Date", key='receptionDate', value=None)
    receptionTime = st.time_input("Reception Time", key='receptionTime', value=None)
    conditionCheck = st.text_area("Condition Check", key='conditionCheck')
    performanceCriteria = st.text_area("Performance Criteria", key='performanceCriteria')
    performanceResult = st.text_area("Performance Result", key='performanceResult')
    notes = st.text_area("Notes", key='notes')
    receivedBy = st.text_input("Received By", key='receivedBy')
    userName = st.text_input("User Name", key='userName')
    performedBy = st.text_input("Performed By", key='performedBy')
    approvedBy = st.text_input("Approved By", key='approvedBy')

    submit = st.form_submit_button("Add Item")

if submit:
    new_item = {
        'itemName': itemName,
        'itemType': itemType,
        'manufacturer': manufacturer,
        'lotNumber': lotNumber,
        'expiryDate': expiryDate,
        'receptionDate': receptionDate,
        'receptionTime': receptionTime,
        'conditionCheck': conditionCheck,
        'performanceCriteria': performanceCriteria,
        'performanceResult': performanceResult,
        'notes': notes,
        'receivedBy': receivedBy,
        'userName': userName,
        'performedBy': performedBy,
        'approvedBy': approvedBy
    }
    st.session_state.items.append(new_item)
    st.success("Item added successfully!")
    reset_form()

# Display filter options
st.sidebar.header("Filters")
filter_item_type = st.sidebar.text_input("Filter by Item Type")
filter_manufacturer = st.sidebar.text_input("Filter by Manufacturer")
filter_perf_result = st.sidebar.text_input("Filter by Performance Result")
search_term = st.sidebar.text_input("Search Item Name")

# Filter data
def filter_items(items):
    filtered = items
    if filter_item_type:
        filtered = [i for i in filtered if filter_item_type.lower() in i['itemType'].lower()]
    if filter_manufacturer:
        filtered = [i for i in filtered if filter_manufacturer.lower() in i['manufacturer'].lower()]
    if filter_perf_result:
        filtered = [i for i in filtered if filter_perf_result.lower() in i['performanceResult'].lower()]
    if search_term:
        filtered = [i for i in filtered if search_term.lower() in i['itemName'].lower()]
    return filtered

filtered_items = filter_items(st.session_state.items)

# Display table of items
st.subheader("Inventory Items")
if filtered_items:
    import pandas as pd
    df = pd.DataFrame(filtered_items)
    st.dataframe(df)
else:
    st.write("No items found.")

# Simple report summary example
st.sidebar.header("Reports")
report_period = st.sidebar.selectbox("Select Report Period", ['Daily', 'Weekly', 'Monthly'])

if st.sidebar.button("Generate Report"):
    count = len(filtered_items)
    st.sidebar.write(f"Total items in report: {count}")
