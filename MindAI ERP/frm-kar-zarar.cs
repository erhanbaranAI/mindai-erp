using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MindAI_ERP
{
    public partial class frm_kar_zarar : Form
    {
        public frm_kar_zarar()
        {
            InitializeComponent();
        }

        private void frm_kar_zarar_Load(object sender, EventArgs e)
        {
            // CSV dosyasını oku ve DataGridView'e yükle 
            // C:\Users\lerha\source\repos\MindAI ERP\MindAI ERP\transactions.csv

            LoadCSVToDataGridView("C:\\Users\\lerha\\source\\repos\\MindAI ERP\\MindAI ERP\\transactions.csv"); 
        }
        private void LoadCSVToDataGridView(string filePath)
        {
            if (!File.Exists(filePath))
            {
                MessageBox.Show("CSV dosyası bulunamadı!", "Hata", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            DataTable dt = new DataTable();
            string[] lines = File.ReadAllLines(filePath);

            if (lines.Length > 0)
            {
                // İlk satır başlıkları içerir, sütunları oluştur
                string[] headers = lines[0].Split(',');
                foreach (string header in headers)
                {
                    dt.Columns.Add(header);
                }

                // Diğer satırları DataTable içine ekleyelim
                for (int i = 1; i < lines.Length; i++)
                {
                    string[] data = lines[i].Split(',');
                    dt.Rows.Add(data);
                }
            }

            // DataGridView'e DataTable'ı bağla
            dgvTransactions.DataSource = dt;
        }
    }
}
