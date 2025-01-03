import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

import pycountry as pct

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('salaries.csv') #Để file dataset cùng 1 folder với file code

#------------BẮT ĐẦU QUÁ TRÌNH TIỀN XỬ LÝ DỮ LIỆU CHO PHÂN TÍCH MÔ TẢ------------

# Tóm lược dữ liệu (Đo mức độ tập trung & mức độ phân tán)
description = data.describe()
mode = data.select_dtypes(include=['float64','int64']).mode().iloc[0]
mode.name = 'mode'
median = data.select_dtypes(include=['float64','int64']).median()
median.name = 'median'
description = description._append(mode)
description = description._append(median)
print(description)

# Kiểm tra tỷ lệ lỗi thiếu data
data_na = (data.isnull().sum() / len(data)) * 100
missing_data = pd.DataFrame({'Ty le thieu data': data_na})
print(missing_data)

# Kiểm tra data bị trùng
duplicated_rows_data = data.duplicated().sum()
print(f"\nSO LUONG DATA BI TRUNG LAP: {duplicated_rows_data}")
data = data.drop_duplicates()

# Quét qua các cột và đếm số lượng data riêng biệt
print("\nSO LUONG CAC DATA RIENG BIET:")
for column in data.columns:
    num_distinct_values = len(data[column].unique())
    print(f"{column}:{num_distinct_values} distinct values")

# Xem qua dataset
print(f"\n5 DONG DAU DATA SET:\n {data.head(5)}")

# Thay đổi giá trị để dataset dễ hiểu hơn
data['experience_level'] = data['experience_level'].replace({
    'SE': 'Senior level',
    'EN': 'Entry level',
    'EX': 'Executive level',
    'MI': 'Mid/Intermediate level'
})

data['employment_type'] = data['employment_type'].replace({
    'FL': 'Freelancer',
    'CT': 'Contractor',
    'FT': 'Full-Time',
    'PT': 'Part-Time'
})

data['company_size'] = data['company_size'].replace({
    'S': 'Small',
    'M': 'Medium',
    'L': "Large"
})

data['remote_ratio'] = data['remote_ratio'].astype(str)  # Chuyển data về dạng chuỗi (ban đầu là dạng số)
data['remote_ratio'] = data['remote_ratio'].replace({
    '0': 'On-site',
    '50': 'Half-Remote',
    '100': 'Full-Remote'
})


# Định nghĩa hàm để gán lĩnh vực cho từng công việc
def assign_broader_category(job_title):
    data_engineering = ["Data Engineer", "Data Analyst", "Analytics Engineer", "BI Data Analyst",
                        "Business Data Analyst", "BI Developer", "BI Analyst", "Business Intelligence Engineer",
                        "BI Data Engineer", "AI Engineer", "AI Research Engineer", "Azure Data Engineer",
                        "BI Data Engineer",
                        "Big Data Engineer", "Cloud Data Engineer", "Cloud Database Engineer",
                        "Computer Vision Engineer",
                        "Computer Vision Software Engineer", "Consultant Data Engineer", "Data Analytics Engineer",
                        "Data DevOps Engineer", "Data Engineer 2", "Data Infrastructure Engineer",
                        "Data Operations Engineer",
                        "Data Quality Engineer", "Data Science Engineer", "Data Visualization Engineer",
                        "Deep Learning Engineer",
                        "ETL Engineer", "Marketing Data Engineer", "ML Engineer", "MLOps Engineer",
                        "NLP Engineer", "Principal Data Engineer", "Research Engineer", "Software Data Engineer"]
    data_scientist = ["Data Scientist", "Applied Scientist", "Research Scientist", "Deep Learning Researcher",
                      "AI Scientist", "Applied Data Scientist",
                      "Decision Scientist", "Principal Data Scientist", "Staff Data Scientist"]
    machine_learning = ["Machine Learning Engineer", "ML Engineer", "Machine Learning Developer",
                        "Applied Machine Learning Engineer",
                        "Machine Learning Engineer", "Machine Learning Infrastructure Engineer",
                        "Machine Learning Research Engineer",
                        "Machine Learning Software Engineer", "Principal Machine Learning Engineer",
                        "Staff Machine Learning Engineer",
                        "Machine Learning Researcher", "Principal Machine Learning Engineer",
                        "Applied Machine Learning Scientist",
                        "Machine Learning Scientist", "Head of Machine Learning", "Lead Machine Learning Engineer"]
    data_architecture = ["Data Architect", "Big Data Architect", "Cloud Data Architect", "Principal Data Architect",
                         "AI Architect", "AWS Data Architect"]
    management = ["Data Science Manager", "Director of Data Science", "Head of Data Science", "Head of Data",
                  "Data Lead", "Data Science Lead",
                  "Data Scientist Lead", "Data Manager", "Data Operations Manager", "Data Analytics Lead",
                  "Data Science Tech Lead",
                  "Lead Data Analyst", "Lead Data Engineer", "Lead Data Scientist"
                                                             "Manager Data Management", "Data Analytics Manager",
                  "Analytics Engineering Manager"]

    if job_title in data_engineering:
        return "Data Engineering"
    elif job_title in data_scientist:
        return "Data Science"
    elif job_title in machine_learning:
        return "Machine Learning"
    elif job_title in data_architecture:
        return "Data Architecture"
    elif job_title in management:
        return "Management"
    else:
        return "Other"

# Áp dụng hàm và tạo cột 'jobs_role'
data['job_role'] = data['job_title'].apply(assign_broader_category)
print(data)  # Check lại dataset sau khi chuyển đổi dữ liệu ở terminal

#------------KẾT THÚC QUÁ TRÌNH TIỀN XỬ LÝ DỮ LIỆU CHO PHÂN TÍCH MÔ TẢ------------

#------------BẮT ĐẦU QUÁ TRÌNH PHÂN TÍCH MÔ TẢ------------

# Biểu đò 1: Biểu đồ hình tròn phân bổ lĩnh vực làm việc (PTMT: Đơn biến - dữ liệu phi số)
job_role = data['job_role'].value_counts().sort_values(ascending=True)
fig1 = px.pie(values=job_role.values,
              names=job_role.index,
              color=job_role.index,
              title="BIỂU ĐỒ HÌNH TRÒN PHÂN BỔ LĨNH VỰC LÀM VIỆC")
fig1.update_traces(textinfo='label+percent+value',
                    textposition='outside')
fig1.show()

# Biều đồ 2: Biểu đồ displot dữ liệu lương tính theo USD (PTMT: Đơn biến - dữ liệu số)
fig2 = ff.create_distplot(hist_data=[data['salary_in_usd']],
                          group_labels=['salary_in_usd'],
                          bin_size=20000,
                          curve_type='kde')
fig2.update_layout(xaxis_title='Lương (USD)',
                   yaxis_title='Tần suất (Đã hiệu chỉnh)',
                   title='BIỂU ĐỒ DISPLOT CỦA LƯƠNG (USD)')
fig2.show()

# Biểu đồ 3: Biểu đồ boxplot phân bổ lương (USD) theo chế độ làm việc (PTMT: Đa biến (2) - dữ liệu hỗn hợp)
fig3 = px.box(data_frame=data,
              x = 'employment_type',
              y= 'salary_in_usd',
              color='employment_type',
              title='BIỂU ĐỒ BOXPLOT PHÂN BỔ LƯƠNG (USD) THEO CHẾ ĐỘ LÀM VIỆC')
fig3.update_layout(xaxis_title='Chế độ làm việc',
                   yaxis_title='Lương (USD)')
fig3.show()

# Biểu đồ 4: Biểu đồ heatmap phân bổ trung bình lương (USD) theo từng năm đối với mỗi mảng làm việc (PTMT: Đa biến (3) - dữ liệu hỗn hợp)
pivot_table = data.pivot_table(values='salary_in_usd',
                               index='job_role',
                               columns='work_year',
                               aggfunc='median')
fig4 = px.imshow(pivot_table,
                 labels=dict(x='Năm', y='Lĩnh vực làm việc'),
                 x=pivot_table.columns,
                 y=pivot_table.index,
                 text_auto='.2f',
                 color_continuous_scale='Viridis',
                 title='BIỂU ĐỒ HEATMAP PHÂN BỔ TRUNG BÌNH LƯƠNG (USD) THEO TỪNG NĂM VỚI MỖI MẢNG LÀM VIỆC')
fig4.show()

# Biểu đồ 5: Biểu đồ Scatter thể hiện mức lương ảnh hưởng bởi nơi ở của nhân viên và công ty (PTMT: Đa biến (3) - dữ liệu hỗn hợp)
fig5 = px.scatter(data_frame=data,
                  x='employee_residence',
                  y='company_location',
                  color='salary_in_usd',
                  size='salary_in_usd', opacity=0.5,
                  labels={'employee_residence': 'Nơi ở nhân viên', 'company_location': 'Nơi làm việc',
                          'salary_in_usd': 'Lương (USD)'},
                  hover_data=['salary_in_usd'],
                  title='BIỂU ĐỒ MỨC LƯƠNG ẢNH HƯỞNG BỞI NƠI Ở NHÂN VIÊN VÀ ĐỊA ĐIỂM CÔNG TY')
fig5.show()


# Biểu đồ 6: Biểu đồ địa lý thể hiện mức lương trung bình theo vị trí công ty (PTMT: Đa biến (2) - dữ liệu hỗn hợp)
# Hàm chuyển đổi code quốc gia thành tên quốc gia
def country_code_to_name(country_code): #Hàm 1
    try:
        return pct.countries.get(alpha_2=country_code).name  # Nếu khả dụng trong thư viện thì chuyển về tên quốc gia
    except:
        return country_code  #Còn không thì giữ nguyên để xử lý theo hàm 2
def country_code_to_name(code): #Hàm 2
    try:
        country = pct.countries.get(alpha_2=code)
        return country.name
    except:
        return None
data['company_location'] = data['company_location'].apply(country_code_to_name)
avg_salary_by_location = pd.DataFrame(data.groupby('company_location', as_index=False)['salary_in_usd'].mean())
fig6 = px.choropleth(data_frame=avg_salary_by_location,
                     locations='company_location',
                     locationmode='country names',
                     color='salary_in_usd',
                     hover_name='company_location',
                     color_continuous_scale='Plasma',
                     title='BIỂU ĐỒ ĐỊA LÝ THỂ HIỆN MỨC LƯƠNG TRUNG BÌNH THEO VỊ TRÍ CÔNG TY',
                     labels={'salary_in_usd': 'Lương trung bình (USD)', 'company_location': 'Vị trí'},
                     projection='natural earth')
fig6.show()

#------------KẾT THÚC QUÁ TRÌNH PHÂN TÍCH MÔ TẢ------------

#------------BẮT ĐẦU QUÁ TRÌNH TIỀN XỬ LÝ DỮ LIỆU CHO PHÂN TÍCH HỒI QUY TUYẾN TÍNH------------

data = data[['work_year', 'experience_level', 'employment_type', 'job_title', 'salary_in_usd',
             'employee_residence', 'remote_ratio', 'company_location', 'company_size']] #Loại bỏ 'salary' và 'salary_currency'
labels_to_encode = ['experience_level', 'employment_type', 'job_title', 'employee_residence', 'remote_ratio', 'company_location', 'company_size'] #Các cột phi số
for label in labels_to_encode:
    data = data.join(pd.get_dummies(data[label],prefix=label))
    data.drop(label, axis=1, inplace=True)
X = pd.DataFrame(data.drop('salary_in_usd', axis=1))
Y = pd.DataFrame(data['salary_in_usd'])

#------------KÉT THÚC QUÁ TRÌNH TIỀN XỬ LÝ DỮ LIỆU CHO PHÂN TÍCH HỒI QUY TUYẾN TÍNH------------

#------------BẮT ĐẦU PHÂN TÍCH HỒI QUY TUYẾN TÍNH------------

model = LinearRegression()
model.fit(X,Y)
r2 = model.score(X,Y)
print("R-square score: ", r2)

#------------KẾT THÚC PHÂN TÍCH HỒI QUY TUYẾN TÍNH------------
