import streamlit as st
import time

st.title('Streamlit 入門')

st.write('プログレスバーの表示')

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration : {i+1}')
    bar.progress(i+1)
    time.sleep(.01)

left_column,right_column=st.beta_columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('test')

# アコーディオン
expander1=st.beta_expander('問い合わせ1')
expander1.write('問い合わせ回答1')
expander2=st.beta_expander('問い合わせ2')
expander2.write('問い合わせ回答2')



text=st.text_input('あなたの趣味を入力してください')
'あなたの趣味は',text,'です'
condition=st.slider('あなたの今の調子は？',0,100,50)
'コンディション：',condition

# df=pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
# )

# st.table(df.style.highlight_max(axis=0))
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)
# st.map(df)

# インタラクティブ
# if st.checkbox('Show Image'):
#     img=Image.open('vangoghmuseum-n0087V1962-800.jpg')
#     st.image(img,caption='image',use_column_width=True)

# option=st.selectbox(
#     '好きな数字を入力してください',
#     list(range(1,11))
# )
# '入力値は',option,'です'

# text=st.sidebar.text_input('あなたの趣味を入力してください')
# condition=st.sidebar.slider('あなたの今の調子は？',0,100,50)
