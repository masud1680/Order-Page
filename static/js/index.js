
               // Load all orders from Django context
      let jsonSiteData = JSON.parse('{{ jsonSiteData_json|escapejs }}');
      console.log(jsonSiteData);

          // Example: send it back to Django
      function sendBack(updatedData) {

          fetch("{% url 'content-dashboard' %}", {
              method: "POST",
              headers: {
                  "Content-Type": "application/json",
                  "X-CSRFToken": "{{ csrf_token }}",
              },
              body: JSON.stringify(updatedData)  // sending Django variable back
          })
          .then(res => res.json())
          .then(result => {
              console.log("Django response:", result);
          });
      }




  // template working section
          document.addEventListener('DOMContentLoaded', function () {
              // --- SIDEBAR LOGIC (UNCHANGED) ---
              const sidebar = document.getElementById('sidebar'); /* ... and so on */
              const mobileMenuBtn = document.getElementById('mobile-menu-btn');
              const desktopSidebarToggle = document.getElementById('desktop-sidebar-toggle');
              mobileMenuBtn.addEventListener('click', () => document.getElementById('nav-menu').classList.toggle('hidden'));
              desktopSidebarToggle.addEventListener('click', () => {
                  if (sidebar.classList.contains('md:w-64')) {
                      sidebar.classList.remove('md:w-64'); sidebar.classList.add('w-0');
                      desktopSidebarToggle.classList.remove('sidebar-open-btn-transform');
                      setTimeout(() => sidebar.classList.add('hidden'), 300);
                  } else {
                      sidebar.classList.remove('hidden');
                      setTimeout(() => { sidebar.classList.remove('w-0'); sidebar.classList.add('md:w-64'); desktopSidebarToggle.classList.add('sidebar-open-btn-transform'); }, 10);
                  }
              });
              if (sidebar.classList.contains('md:w-64')) { desktopSidebarToggle.classList.add('sidebar-open-btn-transform'); }

              // --- NEW CONTENT PAGE LOGIC ---

              // Sample data simulating what's in your database
              const siteData = jsonSiteData;
              //{
                 // fontSection: { small_title: 'Premium Quality', big_title: 'Unique & Stylish Fonts', font_asset: 'https://placehold.co/800x400/92c952/FFFFFF?text=Font+Asset', details: 'Discover our collection of handcrafted fonts that bring personality and elegance to your projects.' },
                 // featureSection: { first_title: 'Our Features', features_name: ['Easy to Install', 'Multi-Language Support', 'Commercial License Included'], second_title: 'Your Benefits', benefits_name: ['Save Time', 'Reach a Global Audience', 'Use on Unlimited Projects'] },
                 // gellerySection: { title: 'Our Font Gallery', description: 'See our fonts in action in these beautiful designs.', photos: [{id:1, name: 'gallery1', photo_asset: 'https://placehold.co/400x400/771796/FFFFFF?text=1'}, {id:2, name: 'gallery2', photo_asset: 'https://placehold.co/400x400/24f355/FFFFFF?text=2'}, {id:3, name: 'gallery3', photo_asset: 'https://placehold.co/400x400/d32776/FFFFFF?text=3'}] },
                 // productDetails: { name: 'Premium Font Pack', quantity: 1, price: 49, insideDhaka: 5, outsideDhaka: 10 },
                 // contactSection: { title: 'Have a question?', number: '+880 1234 567890' }
              //};



              function uploadFile() {
                let fileInput = document.getElementById("font-asset-upload");
                let ffile = fileInput.files[0];   // ✅ now file exists
                if (!ffile) {
                        alert("Please choose a file first!");
                        return;
                    };

                    let font_upimage = new FormData();
                    font_upimage.append("file", ffile);
                    

          };

              // Get all input elements
              const inputs = {
                  fontSmallTitle: document.getElementById('font-small-title'),
                  fontBigTitle: document.getElementById('font-big-title'),
                  fontDetails: document.getElementById('font-details'),
                  fontAssetPreview: document.getElementById('font-asset-preview'),
                  featureFirstTitle: document.getElementById('feature-first-title'),
                  featureList: document.getElementById('feature-list'),
                  featureSecondTitle: document.getElementById('feature-second-title'),
                  benefitList: document.getElementById('benefit-list'),
                  galleryTitle: document.getElementById('gallery-title'),
                  galleryDescription: document.getElementById('gallery-description'),
                  galleryGrid: document.getElementById('gallery-preview-grid'),
                  productName: document.getElementById('product-name'),
                  productQuantity: document.getElementById('product-quantity'),
                  productPrice: document.getElementById('product-price'),
                  productInsideDhaka: document.getElementById('product-inside-dhaka'),
                  productOutsideDhaka: document.getElementById('product-outside-dhaka'),
                  contactTitle: document.getElementById('contact-title'),
                  contactNumber: document.getElementById('contact-number'),
              };

              // Function to populate form fields with data
              function populateForms() {
                  inputs.fontSmallTitle.value = siteData.fontSection.small_title;
                  inputs.fontBigTitle.value = siteData.fontSection.big_title;
                  inputs.fontDetails.value = siteData.fontSection.details;
                  inputs.fontAssetPreview.src = `/media/${siteData.fontSection.font_asset}`;
                  inputs.featureFirstTitle.value = siteData.featureSection.first_title;
                  inputs.featureList.value = siteData.featureSection.features_name.join('\n');
                  inputs.featureSecondTitle.value = siteData.featureSection.second_title;
                  inputs.benefitList.value = siteData.featureSection.benefits_name.join('\n');
                  inputs.galleryTitle.value = siteData.gellerySection.title;
                  inputs.galleryDescription.value = siteData.gellerySection.description;
                  inputs.productName.value = siteData.productDetails.name;
                  inputs.productQuantity.value = siteData.productDetails.quantity;
                  inputs.productPrice.value = siteData.productDetails.price;
                  inputs.productInsideDhaka.value = siteData.productDetails.insideDhaka;
                  inputs.productOutsideDhaka.value = siteData.productDetails.outsideDhaka;
                  inputs.contactTitle.value = siteData.contactSection.title;
                  inputs.contactNumber.value = siteData.contactSection.number;

                  // Populate gallery images
                  inputs.galleryGrid.innerHTML = '';
                  siteData.gellerySection.photos.forEach(photo => addImageToGalleryPreview(photo.photo_asset, photo.id));
              }

              function addImageToGalleryPreview(src, id) {
                   const imgContainer = document.createElement('div');
                  imgContainer.className = 'relative group';
                  imgContainer.dataset.photoId = id;
                  imgContainer.innerHTML = `<img src="/media/${src}" class="w-full h-24 object-cover rounded-md"><button class="absolute top-1 right-1 bg-red-500 text-white rounded-full w-5 h-5 flex items-center justify-center text-xs opacity-0 group-hover:opacity-100 transition-opacity gallery-delete-btn">&times;</button>`;
                  inputs.galleryGrid.appendChild(imgContainer);
                  //console.log(src);
              }

              // --- EVENT LISTENERS ---
              document.getElementById('publish-changes-btn').addEventListener('click', () => {
                  // In a real app, you would gather all data and send to your server
                    uploadFile();
                  alert("Changes Published! (Check the browser console to see the data object).");
                  const updatedData = {
                      fontSection: { small_title: inputs.fontSmallTitle.value, big_title: inputs.fontBigTitle.value, details: inputs.fontDetails.value, font_asset:font_upimage /* etc. */ },
                      featureSection: {first_title:inputs.featureFirstTitle.value, features_name: inputs.featureList.value.split('\n').filter(Boolean),second_title:inputs.featureSecondTitle.value, benefits_name: inputs.benefitList.value.split('\n').filter(Boolean), /* etc. */ },
                      contactSection:{
                                  "title": inputs.contactTitle.value,
                                  "number": inputs.contactNumber.value
                              },
                      productDetails:{
                                  "name": inputs.productName.value,
                                  "quantity": inputs.productQuantity.value,
                                  "price": inputs.productPrice.value,
                                  "insideDhaka": inputs.productInsideDhaka.value,
                                  "outsideDhaka": inputs.productOutsideDhaka.value
                              },
                  };
                  console.log("Saving updated data:", updatedData);
                  sendBack(updatedData);

              });

              document.getElementById('discard-changes-btn').addEventListener('click', () => {
                  if(confirm("Are you sure you want to discard changes?")) populateForms();
              });

              // Image preview handler
              document.getElementById('font-asset-upload').addEventListener('change', function(){ if(this.files[0]) inputs.fontAssetPreview.src = URL.createObjectURL(this.files[0]); });
              document.getElementById('gallery-upload').addEventListener('change', function(){
                  for(const file of this.files) { addImageToGalleryPreview(URL.createObjectURL(file), 'new'); };
              });

              // Gallery delete handler
              inputs.galleryGrid.addEventListener('click', function(e){
                  if(e.target.classList.contains('gallery-delete-btn')) {
                      e.target.parentElement.remove();
                  };
              });

              // Initial population
              populateForms();
          });
