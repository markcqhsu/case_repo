## 案例標題
BF Integrated Production System: Automatic Roll Labels, Central Server, Live Dashboard and Shift Summary, Raising Output from 5.6 to 9+ Boxes/Hour

## 案例摘要
Previously, roll-core labels on the BF machines were handwritten, production data was scattered across several places, and supervisors had to walk to the floor to check machine status. The Production Planning team therefore built one integrated system. It consists of a Label Station on a tablet that prints labels automatically, a central server that receives every roll, a live dashboard that supervisors can open from a phone or computer on the same network, shift summaries with historical data, and a unit converter based on a central BOM. The results: operators work faster, handwriting and errors are reduced, and output has risen from 5.6 boxes per hour to more than 9 boxes per hour. Four machines (BF12 to BF15) are installed now.

## 案例分類
Production systems, Central database, Real-time production monitoring, Factory automation

## 需求單位
BF production team, shift leaders and factory management

## 負責單位
Production Planning

## 案例負責人
Production Planning team

## 案例狀態
In production use on BF12 to BF15. Installation on BF09 is pending because it is an older machine without a mounting bracket.

## 適用地區
Hon Chuan FD Packaging factory, Thailand

## 網站連結

## 影片介紹

## 畫面截圖

## 問題背景
- Roll-core labels were handwritten, which was slow, error-prone and hard to trace afterwards
- Production data was spread across several places, and it was unclear which job ran on which machine, how much it produced, and who operated it
- Supervisors had to walk to the floor to check machine status, which led to coordination errors and wasted time
- Shift summaries took a long time, and waste conversion between units was done by hand
- Average output was 5.6 boxes per hour

## 核心問題
How can label printing, data recording and machine status tracking become one real-time system, so that operators do not handwrite and supervisors do not need to walk to the machines, while output also increases?

## 解決方案
- Label Station on a tablet: enter job data once per run, then print every roll label automatically with roll numbers assigned
- Central server (Node.js, port 4000) receives every roll and job-end summary, stores them in files, and passes them to the dashboard immediately
- Real-time live dashboard: machine status, operator, job code, SO and customer, roll and box counts, speed against the 9 boxes/hour target, and a shift timeline
- Run and idle minutes per machine within the shift, calculated from the gaps between rolls, showing where machines stop
- Automatic shift summary, copy to LINE in one step, and Excel export, including every job per machine
- Full historical record of every roll and job, so problem jobs can be traced immediately
- Unit converter for kg, m, pcs, boxes and rolls, using the same BOM, with a QR Code at each station
- Speed target of 9 boxes/hour shown for every machine on the dashboard

## 執行流程
- The operator enters job data on the tablet and presses print, then prints every roll until the job is finished
- At job end, the operator enters good pieces and waste (kg); the system converts waste to pieces and meters automatically
- The server receives the data and the live dashboard shows the status immediately
- Supervisors check status from a phone or computer on the same network instead of walking to the machines
- At the end of the shift, the system generates the summary, which can be copied to LINE or exported to Excel
- If a job has a problem, the historical record of its rolls and jobs can be checked immediately

## 主要功能
- Live dashboard｜Status of every machine, operator, job code, SO, customer, roll and box counts for today, speed, and shift timeline
- Run and idle minutes｜Shown per machine for the shift, with the longest idle gaps
- Summary by job code｜Good pieces and waste combined across all machines running the same job code
- Shift summary｜Saved automatically, copied to LINE, and exported to Excel
- Historical data｜Every roll and job is stored and can be searched and verified
- Unit converter｜Enter one value (kg, m, pcs or boxes) and get the rest from the same BOM
- Speed target｜9 boxes/hour, compared on the dashboard

## AI 的應用方式
- AI helped develop and adjust the whole system: the label station, server, dashboard, unit converter and shift summary
- AI analysed historical roll data to find idle periods and output per machine
- AI helped design the dashboard for supervisors who check it on their phones, and helped produce the training video

## 使用工具
- Label Station (HTML)｜Label printing page on the tablet
- Zebra｜Label printer on the roll core
- Node.js server｜Receives and stores data, serves the dashboard and BOM
- Live dashboard (HTML)｜Real-time dashboard for supervisors
- BOM (Excel)｜Central unit-conversion database
- QR Code｜Opens the unit converter at each machine

## 執行成果
- Output increased from 5.6 to more than 9 boxes per hour
- Four machines installed (BF12 to BF15), and data from all four reaches the server
- Labels print automatically, reducing handwriting and errors
- Supervisors see machine status in real time without walking to the floor
- Shift summaries are faster, with historical data available for verification
- Operators are happy with the system, and the BF09 operators have asked for it to be installed too

## 產生價值
- For operators｜Work faster, with less handwriting and calculation
- For supervisors and coordinators｜Real-time machine status reduces coordination errors
- For production and management｜Higher output and historical data for decisions
- For the company｜A central production database as the foundation for a future MES connection

## 可複製與延伸應用
- Install on BF09 once a suitable mounting bracket is available for the older machine
- Apply the same design to other machines or lines that use the same station and BOM
- Add automatic email delivery of shift summaries and a phone-friendly dashboard page for supervisors
- Connect to an MES when ready

## 使用限制與注意事項
- Devices must be on the same Wi-Fi network as the server, and port 4000 must be opened in the firewall, which requires an administrator
- Automatic start when the server PC boots is not yet configured; the install script must be run with administrator rights
- The server needs a fixed IP address, to be requested from IT
- Email delivery of shift summaries (SMTP) and time zone settings are waiting for IT configuration
- BF09 is an older machine without a mounting bracket, so a bracket must be prepared before installation
- The 5.6 and 9+ boxes/hour figures are as reported by production; a clear measurement method should be recorded before comparing
- Results depend on the BOM, which must be updated whenever a new job code is added
- Idle periods cannot yet be separated by cause (setup, breakdown or waiting) because the machines do not send status signals
- Data is stored on the server PC and must be backed up regularly

## 成功關鍵
- Operators tested the system and adjusted the screens so they work in practice
- Data is entered once per run, which reduces steps on the floor
- The same BOM is used across the whole system so that numbers match on every screen
- It can be installed and backed up without depending on developers

## 案例關鍵字
BF system, roll labels, central server, live dashboard, real-time, shift summary, run and idle minutes, BOM, unit conversion, QR Code, LINE, Excel, 9 boxes per hour, Production Planning, Hon Chuan FD Packaging, AI
