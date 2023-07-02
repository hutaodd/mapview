import streamlit as st
import pandas as pd
import folium

st.set_page_config(
    page_title="数据地图标点",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# 读取xls表格数据
@st.cache_data
def read_data(file):
    data = pd.read_excel(file)
    return data


def create_heatmap(data, option):  # 创建散点地图
    # 创建地图
    m = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=12)
    # 添加散点图层
    if option == '已完成':
        for index, row in data.iterrows():
            folium.Marker([row['Latitude'], row['Longitude']], popup="已完成",
                          icon=folium.Icon(color='green', icon='ok-sign')).add_to(m)
    if option == '未完成':
        for index, row in data.iterrows():
            folium.Marker([row['Latitude'], row['Longitude']], popup="未完成",
                          icon=folium.Icon(color='red', icon='exclamation-sign')).add_to(m)
    if option == '全部':
        for index, row in data.iterrows():
            if int(row["Status"]) == 1:
                folium.Marker([row['Latitude'], row['Longitude']], popup="已完成",
                              icon=folium.Icon(color='green', icon='ok-sign')).add_to(m)
            else:
                folium.Marker([row['Latitude'], row['Longitude']], popup="未完成",
                              icon=folium.Icon(color='red', icon='exclamation-sign')).add_to(m)

    return m


# 主函数
def main():
    st.sidebar.title("散点地图")

    # 上传xls文件
    file = st.sidebar.file_uploader(
        "上传xls或xls文件,将纬度列头改为Latitude，经度列头改为Longitude,完成状态列头改为Status", type=["xls", "xlsx"])
    option = st.sidebar.selectbox(
        '选择标点类型',
        ('已完成', '未完成', '全部'))
    values = st.sidebar.slider('地图组件大小比例', 0, 100, 100)
    if file is not None:
        # 读取数据
        data = read_data(file)

        # 展示数据
        # st.dataframe(data)

        # 创建热点地图
        m = create_heatmap(data, option)
        values *= 0.01
        st.components.v1.html(m._repr_html_(), width=3840 * values, height=2160 * values)


if __name__ == "__main__":
    main()
