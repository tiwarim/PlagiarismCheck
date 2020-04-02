
        
        // function to create a CORS complaint http request 
        function createCorsRequest(method, url){
            var xhr = new XMLHttpRequest();
            if("withCredentials" in xhr){
                xhr.open(method, url, true);
            } else if (typeof xDomaiRequest != "undefined"){
                xhr = new xDomaiRequest();
                xhr.open(method, url);
            } else{
                xhr = null;
            }
            return xhr;
        }

        /////////////////////////////////////////////////////
        // function that calls for Register
        function makeCorsRequestRegister(uname, pass){
            var url = "https://cors-anywhere.herokuapp.com/ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/register";
            var xhr = createCorsRequest('POST', url)
            const inJson = {
                            "username" : uname ,
                             "password" : pass 
                             };
            const jsonS = JSON.stringify(inJson);
            if(!xhr){
                alert('CORS not supported');
                return;
            }
            xhr.onload = function(){
                var text = xhr.responseText;
              //  alert('Response from Cors requestt')
            };
            xhr.onerror = function(){
                alert('There is an error in calling');
            };
            xhr.setRequestHeader("Content-Type", "application/json");

            xhr.onreadystatechange = function(){
                if(xhr.readyState == 4 && xhr.status == 200){
                var out = JSON.parse(xhr.responseText);
                var main = "";
                var tbltop = `<table>
                                <tr><th>Message</th><th>Status Code</th><th>Tokens left</th></tr>`;
                
                    main += "<tr><td>"+out.message+"</td><td>"+out.statuscode+"</td><td>"+out["tokens left"]+"</td></tr>";
                
                var tblbottom = "</table>";
                var tbl = tbltop + main + tblbottom;
                document.getElementById("register").innerHTML = tbl;
                // alert(out.message);
                }
            };
            
            xhr.send(jsonS);
            
        }

        // sender fnc that takes inputs from the form and calls the api backedn
        function Registersend(){
            var username = document.getElementById("RegisterForm").username.value;
            var password = document.getElementById("RegisterForm").password.value;

            
            makeCorsRequestRegister(username, password);
        }
        /////////////////////////////////////////////




        /////////////////////////////////////////////////////
        // function that calls for Check
        function makeCorsRequestCheck(uname, pass, str1, str2){
            var url = "https://cors-anywhere.herokuapp.com/ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/detect";
            var xhr = createCorsRequest('POST', url)
            const inJson = {
                            "username" : uname ,
                             "password" : pass ,
                             "text1" : str1,
                             "text2" : str2
                             };
            const jsonS = JSON.stringify(inJson);
            if(!xhr){
                alert('CORS not supported');
                return;
            }
            xhr.onload = function(){
                var text = xhr.responseText;
              //  alert('Response from Cors requestt')
            };
            xhr.onerror = function(){
                alert('There is an error in calling');
            };
            xhr.setRequestHeader("Content-Type", "application/json");

            xhr.onreadystatechange = function(){
                if(xhr.readyState == 4 && xhr.status == 200){
                var out = JSON.parse(xhr.responseText);
                var main = "";
                var tbltop = `<table>
                                <tr><th>Message</th><th>Ratio</th><th>Status Code</th><th>Tokens left</th></tr>`;
                
                    main += "<tr><td>"+out.message+"</td><td>"+out["similarity ratio"]+"</td><td>"+out.statuscode+"</td><td>"+out["tokens left"]+"</td></tr>";
                
                var tblbottom = "</table>";
                var tbl = tbltop + main + tblbottom;
                document.getElementById("check").innerHTML = tbl;
                // alert(out.message);
                }
            };
            
            xhr.send(jsonS);
            
        }

        // sender fnc that takes inputs from the form and calls the api backedn
        function Checksend(){
            var username = document.getElementById("RegisterForm").username.value;
            var password = document.getElementById("RegisterForm").password.value;

            var text1 = document.getElementById("CheckForm").text1.value;
            var text2 = document.getElementById("CheckForm").text2.value;
            makeCorsRequestCheck(username, password, text1, text2);
        }
        /////////////////////////////////////////////

        /////////////////////////////////////////////////////
        // function that calls for Refill
        function makeCorsRequestRefill(username, admin_pass, amt){
            var url = "https://cors-anywhere.herokuapp.com/ec2-3-134-112-214.us-east-2.compute.amazonaws.com:8000/refill";
            var xhr = createCorsRequest('POST', url)
            const inJson = {
                            "username" : username ,
                             "admin_password" : admin_pass ,
                             "refill_amt" : Number(amt)
                             };
            const jsonS = JSON.stringify(inJson);
            if(!xhr){
                alert('CORS not supported');
                return;
            }
            xhr.onload = function(){
                var text = xhr.responseText;
              //  alert('Response from Cors requestt')
            };
            xhr.onerror = function(){
                alert('There is an error in calling');
            };
            xhr.setRequestHeader("Content-Type", "application/json");

            xhr.onreadystatechange = function(){
                if(xhr.readyState == 4 && xhr.status == 200){
                var out = JSON.parse(xhr.responseText);
                var main = "";
                var tbltop = `<table>
                                <tr><th>Message</th><th>Status Code</th><th>Tokens left</th></tr>`;
                
                    main += "<tr><td>"+out.message+"</td><td>"+out.statuscode+"</td><td>"+out["tokens left"]+"</td></tr>";
                
                var tblbottom = "</table>";
                var tbl = tbltop + main + tblbottom;
                document.getElementById("refill").innerHTML = tbl;
                // alert(out.message);
                }
            };
            
            xhr.send(jsonS);
            
        }

        // sender fnc that takes inputs from the form and calls the api backedn
        function Refillsend(){
            var username = document.getElementById("RegisterForm").username.value;
            var admin_password = document.getElementById("RefillForm").admin_password.value;
            const refill_amt = document.getElementById("RefillForm").refill_amt.value;
            
            makeCorsRequestRefill(username, admin_password, refill_amt);
        }
        /////////////////////////////////////////////

    