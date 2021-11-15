// is_shortlisted_button = document.getElementById("is_shortlisted_button").onclick(
function myFunction() {
  console.log("jatay")
        document.getElementById("loader_disp").style.visibility ="visible";
        console.log("in myfunction")
      }
      function copy_link(link){
        console.log(link)
        var copyText = link
        // copyText.focus()
        copyText.select();
        document.execCommand("copy");
        alert("Copied the text: " + copyText.value);
        document.getElementById("copy").innerHTML = "Copied";


      }


      function no_companies_func(){
        console.log("in comapys")
        // var copyText = link
        // copyText.focus()
        // copyText.select();
        // document.execCommand("copy");
        alert("No Companies added by customer so can't shortlist");
        // document.getElementById("copy").innerHTML = "Copied";


      }

      
        // document.getElementById("copy").addEventListener('click',function(event){
        //   var copyText = document.getElementById("myInput");
        //   copyText.focus();
        //   copyText.select();
        //   document.execCommand("copy");
        //   // alert("Copied the text: " + copyText.value);
        //   document.getElementById("copy").innerHTML = "Copied"
        //   console.log("in myfunction")


        // })
              
             
            