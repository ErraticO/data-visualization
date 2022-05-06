    $(function () {

				//判断sessionStorage是否有值，有值就把这些值放回到select中
				var ss_schoolClassificationCD = sessionStorage.getItem("schoolClassificationCD");//学校区分CD
				if($.trim(ss_schoolClassificationCD)=="" || ss_schoolClassificationCD==="undefined"!="" || schoolClassificationCD!=null){
					$("#schoolClassificationCD").val(ss_schoolClassificationCD);
				}

				var ss_constructionSpecificity = sessionStorage.getItem("constructionSpecificity");//仕組作り特性
				if($.trim(ss_constructionSpecificity)=="" || ss_constructionSpecificity==="undefined"!="" || ss_constructionSpecificity!=null){
					$("#constructionSpecificity").val(ss_constructionSpecificity);
				}

				var ss_playingStyle = sessionStorage.getItem("playingStyle");//プレイングスタイル
				if($.trim(ss_playingStyle)=="" || ss_playingStyle==="undefined"!="" || ss_playingStyle!=null){
					$("#playingStyle").val(ss_playingStyle);
				}

				var ss_workingMethod = sessionStorage.getItem("workingMethod");//働き方
				if($.trim(ss_workingMethod)=="" || ss_workingMethod==="undefined"!="" || ss_workingMethod!=null){
					$("#workingMethod").val(ss_workingMethod);
				}

               //点击"計算"按钮的时候
			  $("#calculate").click(function(){
			  //先清空以前的错误消息
               $(".errfont").text("");//移除提示中的文字
               $("input[type='text']").removeClass("errbk");//移除文本框红色背景
               $("select").removeClass("errbk");//移除下拉列表红色背景
               //清空计算结果
                $("#calculationResult").val("");

                //获取表单对象中的值
			  	var careerHistory = $("#careerHistory").val();//社歴
			  	var wholeBookNumber = $("#wholeBookNumber").val();//始末書数
				var reflectionBookNumber = $("#reflectionBookNumber").val();//反省書数
				var schoolClassificationCD = $("#schoolClassificationCD").val();//学校区分CD
				var jobsNumber = $("#jobsNumber").val();//転職数
				var constructionSpecificity = $("#constructionSpecificity").val();//仕組作り特性
				var playingStyle = $("#playingStyle").val();//プレイングスタイル
				var workingMethod = $("#workingMethod").val();//働き方
				var workOvertimeAverage = $("#workOvertimeAverage").val();//残業(平均)

                //设置错误标记
                var errorFlag = false;//false代表没有错误
                var mustInputMessage = "必須項目です"
				//错误检验
				 if($.trim(careerHistory)=="" || careerHistory==="undefined"){//社歴
			  		checkErrFunction("careerHistory");
			  		setErrorMessage("careerHistoryMessage",mustInputMessage);
			  		setRedFont("careerHistoryMessage");
					errorFlag = true;
			 	 }
			 	 if($.trim(wholeBookNumber)=="" || wholeBookNumber==="undefined"){//始末書数
                    checkErrFunction("wholeBookNumber");
			  		setErrorMessage("wholeBookNumberMessage",mustInputMessage);
			  		setRedFont("wholeBookNumberMessage");
					errorFlag = true;
			 	 }
			 	 if($.trim(reflectionBookNumber)=="" || reflectionBookNumber==="undefined"){//反省書数
                    checkErrFunction("reflectionBookNumber");
			  		setErrorMessage("reflectionBookNumberMessage",mustInputMessage);
			  		setRedFont("reflectionBookNumberMessage");
					errorFlag = true;
			 	 }
			 	 if($.trim(schoolClassificationCD)=="" ||schoolClassificationCD=="-1" || schoolClassificationCD==="undefined"){//学校区分CD
                    checkErrFunction("schoolClassificationCD");
			  		setErrorMessage("schoolClassificationCDMessage",mustInputMessage);
			  		setRedFont("schoolClassificationCDMessage");
					errorFlag = true;
			 	 }
			 	  if($.trim(jobsNumber)=="" || jobsNumber==="undefined"){//転職数
                    checkErrFunction("jobsNumber");
			  		setErrorMessage("jobsNumberMessage",mustInputMessage);
			  		setRedFont("jobsNumberMessage");
					errorFlag = true;
			 	 }
			 	 if($.trim(constructionSpecificity)=="" ||constructionSpecificity=="-1" || constructionSpecificity==="undefined"){//仕組作り特性
                    checkErrFunction("constructionSpecificity");
			  		setErrorMessage("constructionSpecificityMessage",mustInputMessage);
			  		setRedFont("constructionSpecificityMessage");
					errorFlag = true;
			 	 }
			 	 if($.trim(playingStyle)=="" ||playingStyle=="-1" || playingStyle==="undefined"){//プレイングスタイル
                    checkErrFunction("playingStyle");
			  		setErrorMessage("playingStyleMessage",mustInputMessage);
			  		setRedFont("playingStyleMessage");
					errorFlag = true;
			 	 }
			 	 if($.trim(workingMethod)=="" ||workingMethod=="-1" || workingMethod==="undefined"){//働き方
                    checkErrFunction("workingMethod");
			  		setErrorMessage("workingMethodMessage",mustInputMessage);
			  		setRedFont("workingMethodMessage");
					errorFlag = true;
			 	 }
			 	 if($.trim(workOvertimeAverage)=="" || workOvertimeAverage==="undefined"){//残業(平均)
                    checkErrFunction("workOvertimeAverage");
			  		setErrorMessage("workOvertimeAverageMessage",mustInputMessage);
			  		setRedFont("workOvertimeAverageMessage");
					errorFlag = true;
			 	 }
                   if(errorFlag == true){//如果有错误
                        return;
                   }else{
			 	 	//没有错误设置sessionStorage
					sessionStorage.setItem("careerHistory",careerHistory)//社歴
					sessionStorage.setItem("wholeBookNumber",wholeBookNumber)//始末書数
					sessionStorage.setItem("reflectionBookNumber",reflectionBookNumber)//反省書数
					sessionStorage.setItem("schoolClassificationCD",schoolClassificationCD)//学校区分CD
					sessionStorage.setItem("jobsNumber",jobsNumber)//転職数
					sessionStorage.setItem("constructionSpecificity",constructionSpecificity)//仕組作り特性
					sessionStorage.setItem("playingStyle",playingStyle)//プレイングスタイル
					sessionStorage.setItem("workingMethod",workingMethod)//働き方
					sessionStorage.setItem("workOvertimeAverage",workOvertimeAverage)//残業(平均)
					//没有错误就提交表单
			 	 	$("#form1").submit();

                    }
			  });
		});

    //err提示
    var checkErrFunction=function(idval){
        $("#"+idval).addClass("errbk");
    }

    var setErrorMessage=function(idval,content){
        $("#"+idval).text(content);
    }

    var setRedFont=function(idval){
        $("#"+idval).addClass("redFont");
    }