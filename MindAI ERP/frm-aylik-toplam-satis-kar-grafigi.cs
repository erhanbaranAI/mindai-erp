using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MindAI_ERP
{
    public partial class frm_aylik_toplam_satis_kar_grafigi : Form
    {
        private string pythonExePath = @"C:\Users\lerha\AppData\Local\Programs\Python\Python310\python.exe";
        private string pythonScriptPath = @"C:\Users\lerha\source\repos\MindAI ERP\MindAI ERP\python-api\main.py";
        private string analizKlasoru = @"C:\Users\lerha\source\repos\MindAI ERP\MindAI ERP\analizler\aylik-toplam-satis-ve-kar";
        private string analizTxtPath;
        private string analizGrafikPath;

        public frm_aylik_toplam_satis_kar_grafigi()
        {
            InitializeComponent();
        }

        private async void button1_Click(object sender, EventArgs e)
        {
            await RunPythonAnalysis();
        }

        //private async void btnAnalizEt_Click(object sender, EventArgs e)
        //{
        //    await RunPythonAnalysis();
        //}
        //}

        private async Task RunPythonAnalysis()
        {
            try
            {
                // ✅ Python scriptini çalıştır
                ProcessStartInfo psi = new ProcessStartInfo
                {
                    FileName = pythonExePath,
                    Arguments = $"\"{pythonScriptPath}\"",
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                };

                using (Process process = new Process())
                {
                    process.StartInfo = psi;
                    process.Start();

                    // ✅ Çıktıyı dinle
                    string output = await process.StandardOutput.ReadToEndAsync();
                    string error = await process.StandardError.ReadToEndAsync();
                    process.WaitForExit();

                    // ✅ Python çıktısını kontrol et
                    if (output.Contains("Analiz tamamlandı"))
                    {
                        // ✅ TXT ve resim dosya yollarını belirle
                        analizTxtPath = Path.Combine(analizKlasoru, "analiz_sonucu.txt");
                        analizGrafikPath = Path.Combine(analizKlasoru, "satis_ve_kar_grafik.png");

                        // ✅ Analiz Sonucu TXT dosyasını oku ve ekrana yazdır
                        if (File.Exists(analizTxtPath))
                        {
                            txtAnalizSonucu.Text = File.ReadAllText(analizTxtPath);
                        }

                        // ✅ PictureBox'a Grafiği Yükle
                        if (File.Exists(analizGrafikPath))
                        {
                            pbGrafik.ImageLocation = analizGrafikPath;
                            pbGrafik.SizeMode = PictureBoxSizeMode.StretchImage;
                        }

                        MessageBox.Show("Analiz başarıyla tamamlandı!", "Başarılı", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                    else
                    {
                        MessageBox.Show($"Hata oluştu: {error}", "Hata", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Hata: {ex.Message}", "Hata", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
