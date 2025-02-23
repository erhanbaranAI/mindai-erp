namespace MindAI_ERP
{
    partial class frm_aylik_toplam_satis_kar_grafigi
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.button1 = new System.Windows.Forms.Button();
            this.txtAnalizSonucu = new System.Windows.Forms.RichTextBox();
            this.pbGrafik = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pbGrafik)).BeginInit();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(493, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(169, 67);
            this.button1.TabIndex = 0;
            this.button1.Text = "Analiz et";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // txtAnalizSonucu
            // 
            this.txtAnalizSonucu.Location = new System.Drawing.Point(86, 126);
            this.txtAnalizSonucu.Name = "txtAnalizSonucu";
            this.txtAnalizSonucu.Size = new System.Drawing.Size(270, 368);
            this.txtAnalizSonucu.TabIndex = 1;
            this.txtAnalizSonucu.Text = "";
            // 
            // pbGrafik
            // 
            this.pbGrafik.Location = new System.Drawing.Point(435, 115);
            this.pbGrafik.Name = "pbGrafik";
            this.pbGrafik.Size = new System.Drawing.Size(999, 414);
            this.pbGrafik.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pbGrafik.TabIndex = 2;
            this.pbGrafik.TabStop = false;
            // 
            // frm_aylik_toplam_satis_kar_grafigi
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1477, 679);
            this.Controls.Add(this.pbGrafik);
            this.Controls.Add(this.txtAnalizSonucu);
            this.Controls.Add(this.button1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "frm_aylik_toplam_satis_kar_grafigi";
            this.Text = "frm_aylik_toplam_satis_kar_grafigi";
            ((System.ComponentModel.ISupportInitialize)(this.pbGrafik)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private Button button1;
        private RichTextBox txtAnalizSonucu;
        private PictureBox pbGrafik;
    }
}