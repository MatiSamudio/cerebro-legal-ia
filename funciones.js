async function analizarTexto(modo = "") {
    const texto = document.getElementById("texto").value;
    const archivo = document.getElementById("archivo").files[0];
    const formData = new FormData();
    const spinner = document.getElementById("spinner");
  
    console.log("Modo:", modo);
    console.log("Texto:", texto);
    console.log("Archivo:", archivo);
  
    if (archivo) {
      formData.append("archivo", archivo);
    } else if (texto.trim()) {
      formData.append("texto", texto.trim());
    } else {
      document.getElementById("salida").innerText = "Debe subir un archivo o escribir texto.";
      return;
    }
  
    formData.append("modo", modo);
  
    document.getElementById("salida").innerText = "Analizando...";
    spinner.classList.add("mostrar");
  
    try {
      const response = await fetch("http://localhost:5000/analizar", {
        method: "POST",
        body: formData,
      });
  
      const data = await response.json();
      console.log("Respuesta completa:", data);
  
      document.getElementById("salida").innerText = data.resultado || "No se obtuvo respuesta.";
    } catch (error) {
      document.getElementById("salida").innerText = "Error al conectarse al backend.";
      console.error(error);
    } finally {
      spinner.classList.remove("mostrar");
    }
  }  
  
  function descargarResultado() {
    const texto = document.getElementById("salida").innerText;
    const blob = new Blob([texto], { type: "text/plain" });
    const enlace = document.createElement("a");
    enlace.href = URL.createObjectURL(blob);
    enlace.download = "resultado_cerebrolegal.txt";
    enlace.click();
  }
  