var board = undefined

function connect() {
	ws =  new WebSocket(((window.location.protocol === "https:") ? "wss://" : "ws://") + window.location.host + "/image-stream/"+board);

	ws.onopen = function() {
		console.log("[open] Connection established");
	};
  
	ws.onmessage = async function(e) {
		console.log(`[message] Data received from server`);
		try 
		{
            //console.log(e.data)
            const data = e.data.split("#", 2);

            src = 'data:image/svg+xml;utf8,' + data[1];
            console.log("id= "+data[0] +" size= "+ data[1].length);
            $("#"+data[0]).attr("src",src);
		}
		catch( error ) {
            console.log(error)
        }
		
		
	};
  
	ws.onclose = function(e) {
		if (e.wasClean) {
			console.log(`[close] Connection closed cleanly, code=${e.code} reason=${e.reason}`);
		} else {
			// e.g. server process killed or network down
			// event.code is usually 1006 in this case
			console.log('[close] Connection died');
		}	  setTimeout(function() {
		connect();
	  }, 1000);
	};
  
	ws.onerror = function(err) {
	  console.error('[error] Socket encountered error: ', err.message, 'Closing socket');
	  ws.close();
	};
}



$( document ).ready(function() {

    const urlParams = new URLSearchParams(window.location.search);
    board = urlParams.get('board');
    console.log("board",board)
    if (!board) 
    {
        window.location = "/?board=hello-world"
        return
    }

    //create board
    let template_row = document.querySelector("#row-template").innerHTML;
    let template_func_row = Handlebars.compile(template_row);

    let template_item = document.querySelector("#item-template").innerHTML;
    let template_func_item = Handlebars.compile(template_item);

    let template_button = document.querySelector("#button-template").innerHTML;
    let template_func_button = Handlebars.compile(template_button);

    $.ajax({
        dataType: "json",
        url: "/config/"+board,
        async: false, 
        success: function(data) {
            var l = data.infrastructure.length
            for (var i = 0;i < l;i++)
            {
                row_id = "row"+parseInt(i/4)
                if (i % 4 == 0)
                {
                    //Add row
                    row_obj = template_func_row({"id" : row_id})
                    $("#items").append(row_obj)
                }
                item = data.infrastructure[i]
                console.log("item",item)
                item_obj = template_func_item({"board" : board, "id" : item.id , "name" : item.name })
                $("#"+row_id).append(item_obj)

                var cl = item.commands.length
                for(var j = 0;j < cl;j++)
                {
                    cmd = item.commands[j]
                    cmd_obj = template_func_button({"id" : item.id , "cmd" : cmd.cmd , "text" : cmd.text , "color" : cmd.color})
                    $("#"+item.id+"_commands").append(cmd_obj)
                }

            }
        }
    });




    $(".control").click(function(ev){
        ev.preventDefault()
        id = $(this).data("id")
        cmd = $(this).data("cmd")
        console.log( "Post",board,id,cmd );
        
        $.ajax({
            url: "/control/"+board,
            data : JSON.stringify({ id: id, cmd: cmd }),
            contentType : 'application/json',
            type : 'POST',
            success: function (data) {
                console.log( data );
            }
        });
    });


    //Websocket
	connect()


});
