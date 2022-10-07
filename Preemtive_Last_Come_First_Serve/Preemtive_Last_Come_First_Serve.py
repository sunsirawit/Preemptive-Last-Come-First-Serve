import pandas as pd

d = pd.read_csv('test.csv')
pro_all = d.to_numpy().tolist()
total = len(pro_all)

suc_process = 0 #จำนวนงานที่เสร็จ
x = 0 #ตัวนับโปรเซส
cur_t = 0 #จำนวน burst time ทั้งหมด
temp = [] #ข้อมูลของงาน
time_count = [] #ตัวนับเวลา
time_count.append(0)
output = []

def cal_proc(process): #เช็คจำนวนงาน
    if process[1] >= 1:
        process[1] -= 1
        return process #บันทึกค่า

while suc_process < total: #ในขณะที่จำนวนงานที่เสร็จยังไม่เท่ากับงานทั้งหมด
    if pro_all[x][2] <= cur_t:
        while True: #ลูปจนกว่าตัวต่อไปจะไม่มี == None
            pro_all[x] = cal_proc(pro_all[x]) #นำค่าไปคำนวน
            output.append(pro_all[x]) #นำค่าแสดงออก
            cur_t += 1 #เพิ่มเวลา
            time_count.append(cur_t) #เพิ่มในตัวนับเวลา
            if pro_all[x][1] == 0: #ถ้าโปรเซสเปน 0 ให้ suc += 1
                suc_process += 1
    
            if pro_all[x] == pro_all[-1]: #ถ้าตัวที่ทำยังเปนตัวสุดท้าย
                if pro_all[x][1] == 0: #ถ้าเบิร์สไทม์ตัวสุดท้ายเท่ากับ 0 ให้ออก
                    break
                pass
            elif pro_all[x+1][2] <= cur_t: #ถ้าตัวต่อไปน้อยกว่าหรือเท่ากับเวลาที่กำลังทำงานอยู่
                x += 1 #ให้ทำงานโปรเซสต่อไป
                break

    if pro_all[x][1] == 0: #ถ้าเบิร์สไทม์ปัจจุบันเท่ากับ 0 ให้ทำการ pop ตัวที่เสร็จออก
        total_now = len(pro_all)
        for i in range(total_now):
            if pro_all[i][1] == 0:
                pro_all.pop()
        x -= 1

#print(time_count)
for i in output:
    print(f"{i} \n")

print(pro_all)   