import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
# import pathlib
import time
st.title('Streamlit 超入門')

# st.write('DataFlame')
st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'準備はいいかな？ {1+i}')
    bar.progress(i + 1)
    time.sleep(0.1)

# ----------------------------------------------------------------------------------------------------
### インタラクティブについて参照URL(Refarence)
### https://docs.streamlit.io/en/stable/api.html#display-interactive-widgets

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=["lat","lon"]
)


###  beta.columnによるカラム作成は下記URL参照
## https://docs.streamlit.io/en/stable/api.html#add-widgets-to-sidebar
left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.map(df)


# beta.expanderは、問い合わせ内容などのフォルムに使われる。
expander = st.beta_expander('問い合わせ1')
expander.write('AWSアカウントAPIと連携可能です。')
expander = st.beta_expander('問い合わせ2')
expander.write('AzureアカウントAPIと連携可能です。')
expander = st.beta_expander('問い合わせ3')
expander.write('申し訳ございません。\nGCPアカウントAPIと連携不可になります。')


# ### Textボックスの作成
# text = st.text_input('あなたの趣味を教えてください。')

# ### スライダー(数値の選択)の作成
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)


# 'あなたの趣味は、', text
# 'コンディション:', condition

### selectボックスの作成
# option = st.selectbox(
#     'あなたの好きな数字を教えてください。',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は、', option, 'です。'

### CheckBoxを作成　｜　imageの
# if st.checkbox('Show Image'):
#     img = Image.open('/Users/ishibashihiroki/Desktop/free_images/sm-StockSnap_ELZU79WHYI.jpeg')
#     st.image(img, caption='ishibashi', use_column_width=True)

# ----------------------------------------------------------------------------------------------------

###  Chatグラフのコマンドについて参照URL(Refarence)
### https://docs.streamlit.io/en/stable/api.html#display-charts


# 地図を表す。
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=["lat","lon"]
# )
# st.map(df)


# 棒グラフ
# st.bar_chart(df)

# 折れ線グラフのした部分を塗りつぶした感じ
# st.area_chart(df)

# 折れ線グラフ
# st.line_chart(df)

### テーブルの作成について参照URL(Refarence)
#   https://docs.streamlit.io/en/stable/api.html#display-data

### テーブルを作成できるが、dataframeのような表zの大きさについての設定値はできない。
# st.write(df)

### 動的なテーブルを作成する際は、dataframe()関数を利用
# st.dataframe(df.style.highlight_max(axis=0))

### 静的なテーブルを作成する際は、table()関数を利用
# st.table(df.style.highlight_max(axis=0))



### マジックコマンドの使用方法
# https://docs.streamlit.io/en/stable/api.html#display-text
# """
# # 章
# ## 節
# ### 頁

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

