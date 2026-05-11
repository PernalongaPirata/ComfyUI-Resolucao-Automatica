# ComfyUI Resolução Automática

A minimalist and smart custom node for ComfyUI that automatically calculates the perfect width, height, and batch size for your `Empty Latent Image` based on an input image's aspect ratio.

Perfect for batch processing and workflows utilizing FLUX, SDXL, or SD 1.5, especially when working with ControlNet.

## BR Nota do Autor / EN Author's Note

**PT-BR:** Eu comecei a mexer com o ControlNet recentemente e vi um problema que achava um saco: padronizar uma resolução específica. Tem vezes que você vai mexer com imagem quadrada, retrato ou paisagem, e ter que mudar os números manualmente para encaixar naquilo é muito chato. Procurei e não achei nada sobre como fazer isso do jeito que eu queria. Então, com a ajuda da IA, fiz essa pequena contribuição! Não sei nada de programação, quem fez tudo isso foi a IA. Se tem alguma coisa no código que pode melhorar eu não sei, mas para a minha finalidade ajudou muito. Vou postar um vídeo junto com um pequeno workflow de exemplo para mostrar como ficou. É uma pequena contribuição da comunidade brasileira! O nome do nó é "Resolução Automática", coloquei em português para dar visibilidade à nossa comunidade e também para eu conseguir achar mais rápido na barra de busca na hora de usar.

**EN:** I recently started playing with ControlNet and found a very annoying problem: standardizing specific resolutions. Sometimes you work with square, portrait, or landscape images, and having to manually change the numbers to fit the aspect ratio every single time was a pain. I searched but couldn't find a node that did exactly what I wanted. So, with the help of AI, I created this small contribution! I don't know anything about programming (AI wrote all the code), so I don't know if it can be improved, but it perfectly solved my problem. I will post a video alongside a small example workflow to show how it looks. This is a small contribution from the Brazilian community! I named the node "Resolução Automática" (Automatic Resolution in Portuguese) to give visibility to our community and to make it easier for me to find it in the search bar.

---

## ✨ Features
* **Auto Aspect Ratio Detection:** Reads your input image and outputs the exact dimensions for Portrait, Landscape, or Square formats.
* **Dynamic Base Size:** Set `custom_base_size` to `0` for perfect FLUX/SDXL resolutions (1024 base: 832x1216, 1216x832, 1024x1024). Type `512` for SD 1.5, and it mathematically calculates the perfect multiples of 8!
* **Batch Size Output:** Automatically reads the amount of images inputted and outputs the `batch_size` directly to your Latent node.
* **Minimalist UI:** No cluttered nodes. Just plug your image in, and let the math do the work.

## 📦 Installation

**Method 1: ComfyUI Manager (Recommended)**
* Go to `Install Custom Nodes` in ComfyUI Manager.
* Search for `Resolução Automática`.
* Click Install and restart ComfyUI.

**Method 2: Manual Git Clone**
1. Navigate to your `ComfyUI/custom_nodes/` directory.
2. Open your terminal or command prompt.
3. Run: `git clone https://github.com/PernalongaPirata/ComfyUI-Resolucao-Automatica.git`
4. Restart ComfyUI.

## 🚀 How to Use
1. Add the node: `Add Node` > `Custom` > `Logic` > `Resolução Automática`.
2. Connect the `IMAGE` output from your `Load Image` node into this node.
3. Right-click your `Empty Latent Image` node and select `Convert width to input`, `Convert height to input`, and `Convert batch_size to input`.
4. Connect the `width`, `height`, and `batch_size` outputs from the "Resolução Automática" node to the Latent node.
5. Set your `custom_base_size` (Leave `0` for FLUX/SDXL, or type `512` for SD 1.5, etc).

*(Note: Add your example video and workflow screenshot here so people can see how to connect the nodes!)*
