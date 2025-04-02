// static/js/fullscreen.js
document.addEventListener('DOMContentLoaded', function () {
    const fullScreenBtn = document.getElementById('btn-fullscreen');
    const fullGraficoBtn = document.getElementById('btn-full-grafico');
  
    if (fullScreenBtn) {
      fullScreenBtn.addEventListener('click', () => {
        const el = document.documentElement;
        if (!document.fullscreenElement) {
          el.requestFullscreen().catch(err => console.error(err));
        } else {
          document.exitFullscreen();
        }
      });
    }
  
    if (fullGraficoBtn) {
      fullGraficoBtn.addEventListener('click', () => {
        const grafico = document.getElementById('grafico-barras');
        if (grafico && !document.fullscreenElement) {
          grafico.requestFullscreen().catch(err => console.error(err));
        } else {
          document.exitFullscreen();
        }
      });
    }
  });