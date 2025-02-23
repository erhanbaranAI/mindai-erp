namespace MindAI_ERP
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void karZararRaporuToolStripMenuItem_Click(object sender, EventArgs e)
        {
            LoadFormIntoPanel(new frm_kar_zarar());
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Maximized; // Uygulama a��l�rken tam ekran ba�lat
            this.FormBorderStyle = FormBorderStyle.FixedDialog; // Kenarlar� sabitle
            this.MaximizeBox = false; // B�y�tme butonunu kald�r
            this.MinimizeBox = false; // K���ltme butonunu kald�r
            LoadFormIntoPanel(new frm_main_dashboard());
        }

        // Formlar� panel1 i�ine y�klemek i�in kullan�lacak metod
        private void LoadFormIntoPanel(Form form)
        {
            panel1.Controls.Clear(); // �nceki formu temizle
            form.TopLevel = false; // Formun ba��ms�z pencere olmamas�n� sa�la
            form.Dock = DockStyle.Fill; // Formu panelin tamam�n� kaplayacak �ekilde ayarla
            panel1.Controls.Add(form); // Formu panele ekle
            form.Show(); // Formu g�ster
        }

        private void anasayfaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            LoadFormIntoPanel(new frm_main_dashboard());
        }

        private void analizEtToolStripMenuItem_Click(object sender, EventArgs e)
        {
            LoadFormIntoPanel(new frm_aylik_toplam_satis_kar_grafigi());
        }
    }
}