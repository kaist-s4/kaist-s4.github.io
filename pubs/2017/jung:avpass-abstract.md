AVPASS is a tool for leaking the detection model 
of Android antivirus (AV) programs, and bypassing 
the AV detection by using the leaked information 
coupled with APK perturbation techniques. AVPASS 
is able to infer not only the detection features, 
but also hierarchy of detection rule chains. 
With help from the leaked model and the built-in 
APK perturbation functions, AVPASS is able to 
disguise any android malware as a benign application. 
Furthermore, using our novel additive mode, AVPASS 
supports safe querying and guarantees that one can 
test if the application will be detected by the AV 
without sending the whole or core parts of application. 
As a result, AVPASS leaked significant detection 
features of commercial AVs and achieved almost 
zero detection from VirusTotal when tested with 
more than 5,000 malware. 

In this talk, we present the entire pipeline of 
the APK perturbation process, leaking model process, 
and auto-bypassing process. In addition, we show 
findings about commercial AVs, including their 
detection features and hierarchy, and inform the 
attendees about the potential weaknesses of modern AVs. 

AVPASS will be demonstrated, showing that it modifies 
real world malware precisely, and allows them to 
bypass all AVs following the leaked model. AVPASS 
will be released with every tool that we have built, 
including the original source code and the related 
test data, to enable researchers to replicate the 
research on their own.

