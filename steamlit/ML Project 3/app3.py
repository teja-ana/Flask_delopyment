import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('banglore.pkl','rb'))